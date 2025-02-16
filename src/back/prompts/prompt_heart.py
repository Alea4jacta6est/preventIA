SYSTEM_HEART = """"""

PROMPT_HEART = """###Instructions

I will provide you with observations data for one patient. Please follow the methodology provided below and output the heart disease risk probability (0-100%). Provide a brief explanation of each component and severity level. Set a therapeutic goal for the patient to reduce a given risk. Provide both patient and doctor with advice to reduce the risk. The advice should contain exact actions to perform enriched with numbers of potential improvements for a given component (like "A balanced diet could reduce cholesterol level by 40%").

Be as specific as possible in terms of advise: 
    - for the doctor: a concrete action for the patient in terms of lifestyle
    - for the patient: a concrete medication to prescribe for a psecific purpose, a concrete analysis to perform for a psecific purpose.

If the patient data is missing on some component, mark `severity_level` as Unknown, alert the healcare professional about the necessity to fill in the missing info through 
    - analisys presciption
    - treatement prescription
    - questionnaire for lifestyle to fill in. 

    ###Methodology by component


Methodology by Component

1. Age

    - Risk increases with age. After 40, risk rises by about 5-10% per decade.
    - Men over 45 and women over 55 have a significantly higher risk.

2. Family History

    - If a first-degree relative had heart disease before age 55 (for men) or 65 (for women), risk increases by 15-20%.

3. Body Mass Index (BMI): 
    -  BMI ≥ 25 kg/m²: Increased risk.
    - Each 1 kg/m² increase in BMI raises the risk by 2-5%.
    - BMI ≥ 30 kg/m²: High risk due to obesity-related inflammation and cholesterol issues.

4. Blood Pressure (Hypertension)

    - Systolic BP ≥ 130 mmHg or Diastolic BP ≥ 80 mmHg: Increased risk.
    -Each 10 mmHg increase in BP raises risk by 10-15%.
    - BP ≥ 140/90 mmHg: Strong indicator of high cardiovascular risk.

5. Cholesterol Levels (LDL, HDL, Triglycerides)

    - High LDL ("bad cholesterol") > 130 mg/dL: Increased risk.
    - Low HDL ("good cholesterol") < 40 mg/dL for men, < 50 mg/dL for women: Increased risk.
    - High Triglycerides > 150 mg/dL: Also contributes to higher risk.

6. Blood Sugar (Diabetes/Prediabetes as a Risk Factor)

    - Fasting glucose ≥ 100 mg/dL: Increased risk.
    - HbA1c ≥ 5.7%: Suggests prediabetes, which doubles heart disease risk.
    - Diabetics have 2-4x higher cardiovascular risk.

7. Smoking

    - Smokers have 2-3x higher risk than non-smokers.
    - Each additional pack-year (1 pack per day for 1 year) increases risk significantly.

8. Physical Activity

    - Sedentary lifestyle increases risk by 20-30%.
    - Regular moderate exercise (150 min/week) can reduce risk by 30-40%.

9. Dietary Habits

    - High saturated fat, trans fat, and sugar intake increases risk.
    - Excess sodium intake (>2,300 mg/day) raises blood pressure, increasing risk by 5-10%.
    - A Mediterranean diet (rich in fruits, vegetables, whole grains, and healthy fats) reduces risk by up to 30%.

10. Alcohol Consumption

    - Excess alcohol (>2 drinks/day for men, >1 drink/day for women) raises blood pressure and cholesterol.
    - Moderate red wine intake (1 glass/day) may slightly improve cardiovascular health.

11. Sleep and Stress
    - Poor sleep (< 6 hours per night) increases the risk by 15-20%.
    - Chronic stress and anxiety raise cortisol levels, leading to hypertension and arterial damage.

###Patient Data:

{patient_data}

Output analysis only for components listed above, your analysis should only focus on diabetes, do not include other issues.

### Potential Primary Risks:"""