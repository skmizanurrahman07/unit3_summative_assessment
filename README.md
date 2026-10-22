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

## Ethical considerations

- The data was already anonymised and contained no information that could be used to identify an individual so there were no ethical concerns.
- However, GDPR and data privacy was consider during this project.

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
