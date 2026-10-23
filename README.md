## Healthcare Insurance Cost Analysis Project

This project set out to explore how Data Analytics and AI tools can be use to extract inside information from raw datasets into meaningful insights that utilise for prediction and decesion manking in data driven organisation and for business success. The healthcare Insurance Cost Analysis Project seeks empirically to explore systematic approach to analyse a full end‑to‑end data analytics and machine learning investigation into healthcare insurance costs
Using a real‑world dataset containing Age, Gender, Body mass index, Somking habit and Geographic location that affect insurance cost. The goal is to understand the drivers of insurance charges and build predictive models capable of estimating cost based on customer attributes. 

# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Dataset Content

* Data collected from (https://www.kaggle.com/datasets/willianoliveiragibin/healthcare-insurance?select=insurance.csv)

## Business Requirements

* Identify the factors that affect insurance cost
* Develop an interactive business intelligence tool

## Hypothesis and how to validate?

- Hypothesis (H1): Smokers have higher insurance charges
- Hypothesis (H2): People with higher BMI have higher insurance charges
- Hypothesis (H3): Including children on an insurance plan increase charges
- Hypothesis (H4): Age of a person influences insurance charges 
- Hypothesis (H5): Geographic region influences insurance charges
- Hypothesis (H6): Sex of a person influences insurance charges

## Project Plan and Development Road map

To meet the business requirements this project follows CRISP-DM Workflow as a standard: 
- Business Understanding 
- Data understanding
- Data preparation
- Modelling
- Evaluation and 
- Deployment

- Step 1: Preparation 
          Setup Vscode environment (IDE), create public Github Repository, upload project with all the required files and folders. 
- Step 2: Data Sourcing
          Gather the required Dataset (Healthcare Insurance Cost) for the project to analysis 
- Step 3: Extract-Transform-Load (ETL) to Python Pandas
          Read the dataset file into a pandas dataframe, where step cleaning and creating new calculated coloumns are performed
- Step 4: Analysis and Visualisation with python Ecosystem
          Analysis include- Probabilities, Statistics and Machine learning algorithm and feature engineering pipeline
          Visualisation include- python, Pandas, Matplotlib, seaborn, plotly, Scikit-learn, Scipy
- Step 5: Business Intelligence and Dashboard design with Power BI
          From Step 3, the clean dataset transfer to Power BI for business intelligence and interactive dash board design and for user interaction. Click this link to access power BI intelligence dashboard. 
        -  Link: https://app.powerbi.com/groups/me/reports/1195b5d4-d22f-41e2-a513-57cf3c25ea8f/255a81ee1aa6d8cefa70?experience=power-bi
- Details data analysis Project work breakdown structure (WBS) in the Project Board. Click this link to access project board. 
          - Link: https://github.com/users/skmizanurrahman07/projects/9
## The rationale to map the business requirements to the Data Visualisations

- Hypothesis (H1): Smokers have higher insurance charges
                   Use histogram to show smokers vs overall charge distribution
                   Correlation matrix to show the correlation
                   Box plot to show the distribution

- Hypothesis (H2): People with higher BMI have higher insurance charges
                   Correlation matrix to show correlation
                   Geographic region influences insurance charges
                   Scatter chart to show the distribution

- Hypothesis (H3): Including children on an insurance plan increase charges
                   Including children on an insurance plan increases charges

- Hypothesis (H4): Age of a person influences insurance charges 
                   Correlation matrix to show correlation

- Hypothesis (H5): Geographic region influences insurance charges
                   Geographic region influences insurance charges

- Hypothesis (H6): Sex of a person influences insurance charges
                   Box plot to show the distribution
  
## Analysis techniques used

Structure Justification:

   - Data cleanup and transform and feature engineering Section 1

   - Visualisation and statistical analysis in Section 2.
   
   - Machine Learning in Section 3

## Use of Generative AI:

   - AI supported: GitHub copilot extention was installed and so did speed up some repetative tasks.

# Ethical Considerations, Data Privacy and Governance

## Ethical Considerations

This project analyses healthcare insurance data to identify factors influencing insurance charges and develop predictive models. Although the dataset was anonymised and publicly available, ethical considerations remain important throughout the data lifecycle.

### Fairness and Bias

Machine learning models can unintentionally reinforce existing biases. The dataset may not fully represent all demographic groups and excludes factors such as medical history, income and occupation. Findings have therefore been interpreted cautiously and should not be used as the sole basis for real-world insurance decisions.

### Transparency and Explainability

All data cleaning, statistical testing, visualisations and machine learning approaches are documented within the project. Feature importance analysis and model evaluation metrics were used to improve transparency and understanding of model behaviour.

### Responsible Use

The predictive models developed in this project are intended for educational and analytical purposes only. Human oversight should always be maintained when applying data-driven recommendations in healthcare or insurance settings.

---

## Data Privacy

The dataset was sourced from Kaggle and contains no personally identifiable information (PII). No names, addresses, contact details, NHS numbers or medical record identifiers were included.

Only the variables necessary for the analysis were used:

- Age
- BMI
- Smoking Status
- Number of Children
- Region
- Insurance Charges

This aligns with the UK GDPR principle of **Data Minimisation** (Article 5(1)(c)).

---

## UK GDPR and Legal Compliance

Although the dataset was anonymised, this project was conducted with reference to the principles of the **UK General Data Protection Regulation (UK GDPR)** and the **Data Protection Act 2018**.

The following UK GDPR principles were considered:

| UK GDPR Principle | Application in this Project |
|------------------|----------------------------|
| Lawfulness, Fairness and Transparency | Data source, methodology and findings are clearly documented. |
| Purpose Limitation | Data used solely for educational, analytical and research purposes. |
| Data Minimisation | Only variables relevant to the project objectives were analysed. |
| Accuracy | Data quality checks and cleaning procedures were performed before analysis. |
| Integrity and Confidentiality | The dataset contains no identifiable personal information and is securely stored within the project repository. |
| Accountability | All analytical decisions, assumptions and methodologies are documented within the notebooks and README. |

References:

- UK GDPR: https://www.legislation.gov.uk/eur/2016/679/contents
- Data Protection Act 2018: https://www.legislation.gov.uk/ukpga/2018/12/contents

---

## Consent and Data Usage

The dataset was obtained from a publicly available Kaggle repository and used in accordance with its published access conditions.

Although individual consent records are not available, the dataset has been anonymised and made publicly accessible for data analysis and educational purposes. Proper attribution has been provided to the dataset owner.

---

## Social Impact

Healthcare insurance analytics can influence pricing strategies, risk assessments and access to services. While data analytics can support better decision-making, predictive models may unintentionally reinforce inequalities if used without appropriate governance and human review.

For this reason, the findings from this project should be viewed as decision-support insights rather than automated decision-making tools.

---

## Use of Generative AI

GitHub Copilot and ChatGPT were used to support coding, documentation and troubleshooting during development. All generated outputs were independently reviewed, tested and validated before inclusion in the project. Responsibility for the final code, analysis and conclusions remains with the project author.
## Limitations & Alternatives:

- Limited data points availble in the csv, other factors could influence the decsion such as medial history, family income etc.

## Unfixed Bugs

* - No unfixed bugs remaining

## Main Data Analysis Libraries

The following libraries are used for this data analysis-

1. `Pandas` - Data Loading, Transformation, and Cleaning
2. `NumPy` - Numerical Computation and Array Operations
3. `Matplotlib` - Multi‑Chart Layouts and Base Visualisation
4. `Seaborn` - Statistical Visualisation
5. `Plotly` - Interactive Visualisations
6. `Scipy` - Statistical Tests and Scientific Computation 
7. `scikit-learn` - Machine Learning Models and Preprocessing 
8. `XGBboost` - Gradient Boosting for High‑Performance ML 
9. `LightGBM` - Fast Gradient Boosting for Large Datasets

## Credits
- [Code institute](https://codeinstitute.net/) - The intial project structure.
- [Kaggle](https://www.kaggle.com/) - Providing the data set used.
- [NHS website](https://www.nhs.uk/conditions/obesity/) - Providing the BMI category definitions.
- [ChatGPT](https://chatgpt.com/) - Help getting handles and making a single legend on a multi chart plots and adding layout changes to Plotly charts.
- [SimpleSteps.guide](https://simplesteps.guide/guides/technology/machine-learning-ai) - My notes I recorded from the Code Institute course.
- Copilot
- code institute students

## Acknowledgements
* Thank you the Code Institute and the staff who contributed and supported LMS contents.
