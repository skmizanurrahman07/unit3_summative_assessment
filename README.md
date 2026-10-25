# Healthcare Insurance Cost Analysis Dashboard
# Code Institute Capstone Project

Live Application

🌐 Heroku Deployment

Healthcare Insurance Cost Analysis Dashboard https://healthcare-insurance-cost-b71903468e94.herokuapp.com/

GitHub Repository

💻 Source Code 

unit3_summative_assessment https://github.com/skmizanurrahman07/unit3_summative_assessment

Power BI Dashboard

📊 Interactive Business Intelligence Dashboard

Healthcare Insurance Cost Power BI Dashboard https://app.powerbi.com/groups/me/reports/1195b5d4-d22f-41e2-a513-57cf3c25ea8f/255a81ee1aa6d8cefa70?experience=power-bi

Project Management Dashboard

📋 GitHub Project Board https://github.com/users/skmizanurrahman07/projects/13/views/1

# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Healthcare Insurance Cost Analysis using Data Analytics, Machine Learning and Business Intelligence

## Project Overview 

The Healthcare Insurance Cost Analysis Dashboard is an end-to-end Data Analytics and Machine Learning project developed as part of the Code Institute Capstone Project.

The project investigates the key factors that influence healthcare insurance costs using:

* Exploratory Data Analysis (EDA)
* Statistical Hypothesis Testing
* Machine Learning
* Power BI Business Intelligence
* Streamlit Dashboard Development
* Ethical Practice and Governance

The objective is to identify the primary drivers of healthcare insurance charges and communicate actionable insights through business intelligence dashboards and predictive modelling.

This project demonstrates the complete data analytics lifecycle from business understanding through deployment and evaluation using real-world healthcare insurance data.

# Business Case

Healthcare insurance providers require a deeper understanding of the factors influencing insurance charges in order to:

* Improve pricing strategies
* Support risk assessment
* Enhance customer segmentation
* Improve business decision-making
* Optimise healthcare cost forecasting

The Healthcare Insurance Cost Analysis project investigates these factors using statistical analysis, machine learning and interactive dashboards.

The project aims to determine whether demographic, behavioural and geographical factors influence healthcare insurance costs and whether machine learning can effectively predict future charges.

# Business Requirements
## Business Requirement 1

Identify the factors affecting healthcare insurance costs.

## Success Criteria
* Perform exploratory data analysis.
* Conduct statistical testing.
* Validate key business hypotheses.
* Identify the strongest insurance cost drivers.

## Business Requirement 2

Develop an interactive business intelligence dashboard.

## Success Criteria
* Present findings visually.
* Allow stakeholder interaction.
* Display machine learning outcomes.
* Communicate business insights effectively.

# Dataset Information
### Dataset Source and collection
The dataset was sourced from Kaggle as a publicly available healthcare insurance dataset containing anonymised records.

https://www.kaggle.com/datasets/willianoliveiragibin/healthcare-insurance

Data collection involved:

* Dataset acquisition
* Data validation
* Dataset quality assessment
* Data suitability review against business requirements

### Dataset Variables

| Variable | Description               |
|----------|---------------------------|
| Age      | Age of the insured person |
| Sex      | Gender                    |
| BMI      | Body Mass Index           |
| Children | Number of dependents      |
| Smoker   | Smoking status            |
| Region   | Geographic region         |
| Charges  | Medical insurance charges |

### Dataset Summary
1338 Records
7 Variables
No missing values
Publicly available and anonymised

# Project Planning and Roadmap

The project followed an iterative and agile development approach managed through GitHub Projects.

### GitHub Project Board

Project planning, sprint management, task tracking and milestone monitoring were completed using GitHub Projects.

Project Board: https://github.com/users/skmizanurrahman07/projects/13/views/1

## Development Roadmap
### Phase 1
Project Setup
* Configure development environment.
*  Create GitHub repository.
*  Create project board.
*  Define business requirements.

### Phase 2
Data Collection
* Source healthcare insurance dataset.
* Assess data quality.
* Validate data suitability.

### Phase 3
Data Preparation
* Data cleaning.
* Data transformation.
* Feature engineering.
* Categorisation.

### Phase 4
Analysis
* Exploratory Data Analysis.
* Statistical testing.
* Correlation analysis.

### Phase 5
Machine Learning
* Linear Regression.
* Random Forest Regression.
* XGBoost.
* LightGBM.

### Phase 6
Business Intelligence
* Power BI dashboard.
* Streamlit dashboard.

### Phase 7
Validation and Documentation
* Business Requirement Validation.
* Ethical Review.
* README documentation.
* Deployment.

## CRISP-DM Methodology
This project follows the Cross Industry Standard Process for Data Mining (CRISP-DM).
1. Business Understanding
* Define objectives and project requirements.

2. Data Understanding
* Investigate dataset structure and data quality.

3. Data Preparation
* Clean, transform and prepare data for analysis.

4. Modelling
* Train machine learning models.

5. Evaluation
* Assess performance and validate findings.

6. Deployment
* Deploy dashboards and documentation.

## Hypothesis and how to validate?

- Hypothesis (H1): Smokers have higher insurance charges
- Hypothesis (H2): People with higher BMI have higher insurance charges
- Hypothesis (H3): Including children on an insurance plan increase charges
- Hypothesis (H4): Age of a person influences insurance charges 
- Hypothesis (H5): Geographic region influences insurance charges
- Hypothesis (H6): Sex of a person influences insurance charges

## Mapping Business Requirements to Data Visualisations

| Business Question | Visualisation                 |
| ----------------- | ----------------------------- |
| Smoking Impact    | Histogram, Feature Importance |
| BMI Impact        | Scatter Plot                  |
| Age Impact        | KPI Analysis, Correlation     |
| Region Impact     | Regional Comparison Chart     |
| Sex Impact        | Statistical Analysis          |
| Machine Learning  | Model Comparison Chart        |


## Technology Stack

### Programming Languages
* Python
### Data Analysis
* `Pandas` - Data Loading, Transformation, and Cleaning
* `NumPy` - Numerical Computation and Array Operations
* `Scipy` - Statistical Tests and Scientific Computation 
### Visualisation
* `Matplotlib` - Multi‑Chart Layouts and Base Visualisation
* `Seaborn` - Statistical Visualisation
* `Plotly` - Interactive Visualisations
### Machine Learning
* `scikit-learn` - Machine Learning Models and Preprocessing 
* `XGBboost` - Gradient Boosting for High‑Performance ML 
* `LightGBM` - Fast Gradient Boosting for Large Datasets
### Business Intelligence
* Power BI
* Streamlit
### Development Tools
* GitHub
* VS Code
* Jupyter Notebook
* Heroku

# Data Preparation and Feature Engineering
### Activities Performed
* Dataset inspection
* Data validation
* Data type verification
* Feature categorisation
* Business logic transformation
* Exploratory checks

### Data Quality
The dataset contained:
* ONE duplicate rows
* No missing values
* Consistent formatting

# Exploratory Data Analysis
DA was undertaken to identify relationships between variables and insurance charges.
### Analysis Conducted
* Descriptive statistics
* Histograms
* Scatter plots
* Correlation analysis
* Regional analysis
* Smoking analysis

# Key Findings

### Smoking Status
* Smoking status is the strongest predictor of healthcare insurance charges.

### BMI
* Higher BMI individuals generally incur higher insurance costs.

### Age
* Insurance costs increase as age increases.

### Region
* Regional differences are present but less influential.

## Sex
* Sex demonstrates limited influence on healthcare charges.

# Statistical Analysis
### H1 Smoking Status
* Welch's T-Test  p-value: 5.89e-103
* Supported Smoking status significantly affects healthcare insurance costs.
### H2 BMI
* ANOVA   p-value:  1.85e-11
* Supported BMI significantly affects healthcare insurance costs.
### H5 Region
* ANOVA   p-value: 0.0309
* Supported Region significantly affects healthcare insurance costs.

# Machine Learning
### Models Evaluated
* Linear Regression
* Random Forest Regression
* XGBoost
* LightGBM

| Model                      | MAE      | RMSE     | R² Score |
|----------------------------|----------|----------|----------|
| Linear Regression          | 4187.32  | 5800.06  | 0.7833   |
| Random Forest Regression   | 2437.57  | 4504.41  | 0.8693   |
| XGBoost Regression         | 2721.45  | 4644.79  | 0.8610   |
| LightGBM Regression        | 2908.04  | 4775.06  | 0.8531   |

### Model Ranking
* Random Forest Regression (R² = 0.8693)
* XGBoost Regression (R² = 0.8610)
* LightGBM Regression (R² = 0.8531)
* Linear Regression (R² = 0.7833)


### Model Comparison

### Best Performing Model
* Random Forest Regression

| Metric    | Value   |
|-----------|---------|
| MAE       | 2437.57 |
| RMSE      | 4504.41 |
| R² Score  | 0.8693  |

# Power BI Dashboard

A business intelligence dashboard was developed using Microsoft Power BI.

Features include:

* Executive Summary
* KPI Reporting
* Regional Insights
* Age Analysis
* BMI Analysis
* Smoking Analysis

* Power BI Dashboard: https://app.powerbi.com/groups/me/reports/1195b5d4-d22f-41e2-a513-57cf3c25ea8f/255a81ee1aa6d8cefa70?experience=power-bi

# Streamlit Dashboard

The Streamlit application provides interactive data exploration and business reporting. https://healthcare-insurance-cost-b71903468e94.herokuapp.com/

Pages include:

* Home
* EDA
* Hypothesis Testing
* Machine Learning
* Ethics
* Business Requirement Validation
* Business Recommendations
* Project Conclusions
* Executive Summary

# Business Requirement Validation
### Requirement 1

Identify the factors affecting healthcare insurance costs.

### Result

✅ Successfully Achieved

Evidence:
* EDA
* Statistical Testing
* Machine Learning
* Feature Importance Analysis

### Requirement 2

Develop an interactive business intelligence tool.

### Result

✅ Successfully Achieved

Evidence:
* Power BI Dashboard
* Streamlit Dashboard
* Interactive Visualisations
* KPI Reporting

## Business Recommendations

Based on the analysis:

### Smoking Intervention Programmes
Encourage smoking cessation programmes.

### Preventive Healthcare
Promote healthier lifestyles and weight management.

### Risk-Based Pricing
Continue using smoking status as a pricing factor.

### Customer Segmentation
Use Age and BMI to support targeted offerings.

### Predictive Analytics
Implement predictive models to support decision-making.

## Executive Summary
### Key Findings
* Smoking Status is the strongest predictor of insurance costs.
* BMI significantly affects insurance charges.
* Age significantly affects charges.
* Region has a moderate effect.
* Sex has limited impact.

## Project Achievements

✅ Business Requirement 1 Successfully Achieved

✅ Business Requirement 2 Successfully Achieved

✅ Statistical Hypotheses Validated

✅ Interactive Power BI Dashboard Developed

✅ Interactive Streamlit Dashboard Developed

✅ Machine Learning Models Evaluated

✅ Ethical, Privacy and Governance Considerations Addressed


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


# Deployment
### Heroku Deployment
The application is deployed using:
* Heroku
* Procfile
* setup.sh
* requirements.txt
* Live Application: https://healthcare-insurance-cost-b71903468e94.herokuapp.com/

# Limitations & Alternatives:
* Dataset contains only 1338 records.
* Dataset excludes medical history.
* Income information is unavailable.
* Family health history is unavailable.
* External healthcare factors are not represented.

# Future Improvements
* Explainable AI (XAI)
* Additional healthcare datasets
* API integration
* Real-time predictions
* Advanced feature engineering
* Automated retraining pipelines

# Use of Generative AI
GitHub Copilot and ChatGPT were used to support:
* Code generation
* Documentation
* Troubleshooting
* Dashboard design

All outputs were reviewed, tested and validated before inclusion.
Responsibility for the final project remains with the author.


## Unfixed Bugs

* - No unfixed bugs remaining

# Credits
- [Code institute](https://codeinstitute.net/) - The intial project structure.
- [Kaggle](https://www.kaggle.com/) - Providing the data set used.
- [NHS website](https://www.nhs.uk/conditions/obesity/) - Providing the BMI category definitions.
- [ChatGPT](https://chatgpt.com/) - Help getting handles and making a single legend on a multi chart plots and adding layout changes to Plotly charts.
- [SimpleSteps.guide](https://simplesteps.guide/guides/technology/machine-learning-ai) - My notes I recorded from the Code Institute course.
- Copilot
- code institute students

### Learning Resources
* Code Institute
* Streamlit Documentation
* Scikit-Learn Documentation
* Plotly Documentation
* Power BI Documentation

### Additional Resources
* NHS BMI Guidance
* UK GDPR Documentation
* Data Protection Act 2018

### Acknowledgements
Special thanks to:
* Code Institute
* Course Facilitators
* Mentors
* Fellow Students
* Open Source Community
* contributor who creates LMS contents.

for the guidance, resources and support provided throughout this project.