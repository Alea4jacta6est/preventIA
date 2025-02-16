# PreventIA

## AI-based Healthcare Assessment Framework

PreventIA is an AI-driven health scoring and risk estimation framework designed to analyze patient history, medical images, and health records to provide actionable insights for doctors and patients. This project leverages historical data analysis and state-of-the-art machine learning models for predictive health assessment.

## Architecture

![Schema Diagram](docs/images/schema.png)

The system is built using Python 3.10 and is structured with both frontend and backend services. The architecture integrates multiple AI models and data sources, including:

- **Mistral Large 2**: Processes patient history and risk estimation rules (e.g., SCORE2-Diabetes).
- **Pixtral Large**: Analyzes medical images such as X-rays and MRIs.
- **MedRAX Agent**: Handles structured reasoning for medical analysis and risk estimation.
- **Agent Router**: Directs patient information to specialized estimators (e.g., heart risk, diabetes risk, arterial hypertension, depression).
- **Risk Assessment Module**: Generates JSON-based scoring per test, providing:
  - Summary per risk type
  - Advice for doctors
  - Personalized action items for patient lifestyle improvements

## Installation

### Prerequisites

- Python 3.10
- Poetry
- OpenAI, Mistral API Keys

### Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/Alea4jacta6est/preventIA.git
   cd preventia
   ```

2. Install dependencies using Poetry:
   ```sh
   poetry install
   ```

3. Run the backend and frontend services:
   ```sh
   make front
   make back
   ```

## Usage

1. Input patient data (EHR, medical images, lifestyle factors).
2. AI models analyze data and generate risk estimations.
3. The system outputs structured JSON-based scoring and summaries.


## Contributors

- Natalia Bobkova
- Victoria Latynina
- Quentin Clément
- Abderrazaq Makran
- Guillaume Deramchi 
- Manech Laguens

## Acknowledgments

Special thanks to the **MedRAX** team for publishing open-source code, models and datasets for clean and reusable X-ray analysis.

