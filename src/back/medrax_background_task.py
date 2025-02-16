"""This script is designed to analyze chest X-ray images from a dataset using an AI agent powered by MedRAX and OpenAI’s GPT-based model. 
It automates the process of image classification and generates structured JSON output containing relevant medical findings."""
import os
import time
import json
import glob
import re
import warnings
from typing import *
from dotenv import load_dotenv
from transformers import logging

from langgraph.checkpoint.memory import MemorySaver
from langchain_openai import ChatOpenAI
from medrax.agent import *
from medrax.tools import *
from medrax.utils import *

# Suppress warnings and set logging verbosity
warnings.filterwarnings("ignore")
logging.set_verbosity_error()
load_dotenv()

# Load API key from environment variables
api_openai = os.getenv("OPENAI_API")
if api_openai is None:
    raise ValueError("Missing OpenAI API Key. Please set it in the .env file.")

def clean_markdown_json(text: str) -> str:
    """
    Remove markdown formatting (e.g., triple backticks) from the text if present.
    """
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
    return text

def initialize_agent(
    prompt_file: str,
    tools_to_use: Optional[List[str]] = None,
    model_dir: str = "/model-weights",
    temp_dir: str = "temp",
    device: str = "cuda",
):
    """Initialize the MedRAX agent with specified tools and configuration."""
    prompts = load_prompts_from_file(prompt_file)
    prompt = prompts["MEDICAL_ASSISTANT"]
    
    all_tools = {
        "ChestXRayClassifierTool": lambda: ChestXRayClassifierTool(device=device)
    }
    
    tools_dict = {tool: all_tools[tool]() for tool in (tools_to_use or all_tools.keys()) if tool in all_tools}
    
    checkpointer = MemorySaver()
    model = ChatOpenAI(model="gpt-4o", temperature=0.7, top_p=0.95, api_key=api_openai)
    
    agent = Agent(
        model,
        tools=list(tools_dict.values()),
        log_tools=True,
        log_dir="logs",
        system_prompt=prompt,
        checkpointer=checkpointer,
    )
    
    print("Agent initialized")
    return agent, tools_dict

def process_image_and_prompt(agent, image_path: str, prompt: str):
    """
    Process a single image with the given prompt using the agent's workflow.
    The final agent response is saved as a JSON file named TEST.json in the same folder as the image.
    """
    messages = [
        {"role": "user", "content": f"path: {image_path}"},
        {"role": "user", "content": prompt},
    ]
    
    final_output = None
    
    try:
        for event in agent.workflow.stream(
            {"messages": messages},
            {"configurable": {"thread_id": str(time.time())}},
        ):
            if isinstance(event, dict) and "process" in event:
                content = event["process"]["messages"][-1].content
                if content:
                    cleaned_content = clean_markdown_json(content)
                    try:
                        final_output = json.loads(cleaned_content)
                    except Exception as parse_error:
                        print(f"Could not parse agent response as JSON: {parse_error}")
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
    
    output_file = os.path.join(os.path.dirname(image_path), "TEST.json")
    
    if final_output is None:
        print("No valid JSON response found; nothing to write.")
    else:
        with open(output_file, "w") as f:
            json.dump(final_output, f, indent=2)
        print(f"Output written to {output_file}")

def main():
    """Main function to initialize the agent and process images from patient folders."""
    print("Starting batch processing...")
    
    selected_tools = ["ChestXRayClassifierTool"]
    agent, _ = initialize_agent("medrax/docs/system_prompts.txt", tools_to_use=selected_tools)
    
    base_data_dir = "/root/users/hackathon_doctolib/data"
    patient_folders = sorted(glob.glob(os.path.join(base_data_dir, "patient_*")))
    
    if not patient_folders:
        print(f"No patient folders found in '{base_data_dir}'. Ensure the directory exists and contains patient folders.")
        return
    
    prompt = "Only return: cardiomegaly, effusion, edema, enlarged cardiomediastinum results as a json file."
    
    for patient_folder in patient_folders:
        image_path = os.path.join(patient_folder, "xray.jpg")
        if os.path.exists(image_path):
            print(f"Processing image: {image_path}")
            process_image_and_prompt(agent, image_path, prompt)
        else:
            print(f"Image not found in {patient_folder}")

if __name__ == "__main__":
    main()
