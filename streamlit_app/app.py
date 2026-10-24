import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="Healthcare Insurance Cost Analysis",
    layout="wide"
)

# ---------------------------------------------------
# Load Data
# ---------------------------------------------------

df = pd.read_csv("data/insurance_cleaned.csv")
# Create Sidebar Navigation
page = st.sidebar.radio(
    "Choose a Section",
    [
        "Home",
        "EDA",
        "Hypothesis Testing",
        "Machine Learning",
        "Ethics",
        "Business Requirement Validation",
        "Business Recommendations",
        "Project Conclusions",
        "Executive Summary"
    ]
)
# Add Home Page
if page == "Home":
# ---------------------------------------------------
# Title
# ---------------------------------------------------
    st.title("Healthcare Insurance Cost Analysis Dashboard")
    st.write("""
               This dashboard explores healthcare insurance costs using:
            - Exploratory Data Analysis
            - Statistical Testing
            - Machine Learning
            - Ethical Data Practices
        """)

    st.header("Project Overview")

    st.write("""
    This project investigates factors affecting
    healthcare insurance costs including:

    - Age
    - BMI
    - Smoking Status
    - Region
    - Number of Children
    """)
    # add footer at the bottom of the page
    st.divider()

    st.caption(
        "Healthcare Insurance Cost Analysis Dashboard | Code Institute Capstone Project"
    )

# Create EDA page

if page == "EDA":

    st.title("Exploratory Data Analysis")

    st.write("""
    In this section, we explore the dataset to understand
    the factors influencing healthcare insurance charges.
    """)
   
   # Filters
    st.sidebar.header("Filters")

    selected_region = st.sidebar.multiselect(
        "Select Region",
        options=df["Region"].unique(),
        default=df["Region"].unique()
    )

    selected_smoker = st.sidebar.multiselect(
        "Smoking Status",
        options=df["Smoker"].unique(),
        default=df["Smoker"].unique()
    )

    filtered_df = df[
        (df["Region"].isin(selected_region)) &
        (df["Smoker"].isin(selected_smoker))
    ]

    # Dataset Preview
    st.subheader("Dataset Preview")
    st.dataframe(filtered_df.head(20))

    # KPI Cards
    st.subheader("Key Performance Indicators")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Average Charge",
            f"${filtered_df['Charges'].mean():,.0f}"
        )

    with col2:
        st.metric(
            "Average BMI",
            f"{filtered_df['BMI'].mean():.1f}"
        )

    with col3:
        st.metric(
            "Average Age",
            f"{filtered_df['Age'].mean():.1f}"
        )

    with col4:
        st.metric(
            "Policyholders",
            f"{len(filtered_df):,}"
        )

    # First Row of Charts
    col_left, col_right = st.columns(2)

    with col_left:

        st.subheader("BMI vs Insurance Charges")

        scatter_fig = px.scatter(
            filtered_df,
            x="BMI",
            y="Charges",
            color="Smoker",
            size="Age",
            hover_data=["Region", "Children"]
        )

        st.plotly_chart(
            scatter_fig,
            use_container_width=True
        )

    with col_right:

        st.subheader("Average Charges by Region")

        region_summary = (
            filtered_df
            .groupby("Region")["Charges"]
            .mean()
            .reset_index()
        )

        region_fig = px.bar(
            region_summary,
            x="Region",
            y="Charges",
            color="Region"
        )

        st.plotly_chart(
            region_fig,
            use_container_width=True
        )

    # Second Row of Charts
    col_left2, col_right2 = st.columns(2)

    with col_left2:

        st.subheader("Insurance Charge Distribution")

        hist_fig = px.histogram(
            filtered_df,
            x="Charges",
            color="Smoker",
            nbins=30,
            barmode="overlay",
            opacity=0.7
        )

        st.plotly_chart(
            hist_fig,
            use_container_width=True
        )

    with col_right2:

        st.subheader("Smoking Status Distribution")

        smoker_counts = (
            filtered_df["Smoker"]
            .value_counts()
            .reset_index()
        )

        smoker_counts.columns = ["Smoker", "Count"]

        pie_fig = px.pie(
            smoker_counts,
            names="Smoker",
            values="Count",
            hole=0.5
        )

        st.plotly_chart(
            pie_fig,
            use_container_width=True
        )
    # add footer at the bottom of the page    
    st.divider()

    st.caption(
        "Healthcare Insurance Cost Analysis Dashboard | Code Institute Capstone Project"
    )
    
# Create Hypothesis page

elif page == "Hypothesis Testing":

    st.title("Hypothesis Testing")

    st.success("""
    H1 Supported

    Smokers have significantly higher insurance charges

    Welch T-Test p-value:
    6.26e-103
    """)

    st.success("""
    H2 Supported

    BMI significantly affects charges

    ANOVA p-value:
    1.54e-11
    """)

    st.success("""
    H5 Supported

    Region significantly affects charges

    ANOVA p-value:
    0.0328
    """)
    
    st.info("""
        Hypothesis Validation Summary

        Five out of six hypotheses were supported or partially
        supported by statistical analysis and machine learning.

        Smoking status, BMI and age consistently emerged as the
        strongest predictors of healthcare insurance costs.

        These findings support the project's business objective
        of identifying the primary drivers of insurance charges.
    """)
    # add footer at the bottom of the page    
    st.divider()
    
    st.caption(
            "Healthcare Insurance Cost Analysis Dashboard | Code Institute Capstone Project"
        )

# Create Machine Learning page:

elif page == "Machine Learning":

    st.title("Machine Learning Results")
    # model comparison chart
    results = pd.DataFrame({
        "Model": [
            "Linear Regression",
            "Random Forest",
            "XGBoost",
            "LightGBM"
        ],
        "R²": [
            0.8068,
            0.8862,
            0.8670,
            0.8745
        ]
    })
    fig = px.bar(
        results,
        x="Model",
        y="R²",
        color="Model",
        title="Machine Learning Model Comparison"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

   # Model Performance Chart

    st.subheader("Model Performance")

    st.dataframe(results)

    st.bar_chart(
        results.set_index("Model")
    )
    st.success("""
    Best Performing Model

    ✅ Random Forest

    R² = 0.8862

    MAE = 2510.28

    RMSE = 4572.72
    """)
    st.info("""
        Why Random Forest?

        Random Forest achieved the highest R² score,
        lowest prediction error and produced feature
        importance rankings that aligned strongly with
        both the statistical analysis and business findings.
    """)

    # Feature Importance Chart

    importance_df = pd.DataFrame({
        "Feature": [
            "Smoking Status",
            "BMI",
            "Age",
            "Children",
            "Region"
        ],
        "Importance": [
            59.8,
            22.2,
            13.9,
            2.4,
            1.6
        ]
    })
    fig = px.bar(
        importance_df,
        x="Importance",
        y="Feature",
        orientation="h",
        color="Feature",
        title="Random Forest Feature Importance"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.info("""
        Feature Importance Interpretation

        Smoking Status accounts for approximately 60% of
        the model's predictive power, confirming it as the
        single most influential factor affecting healthcare
        insurance costs.

        BMI and Age are also significant predictors, while
        Region and Children contribute comparatively less.
    """)

    # add footer at the bottom of the page
    st.divider()

    st.caption(
        "Healthcare Insurance Cost Analysis Dashboard | Code Institute Capstone Project"
    )

# Create Ethics page:

elif page == "Ethics":

    st.title("Ethics, Privacy and Governance")

    st.markdown("""
    ## UK GDPR
    The UK General Data Protection Regulation (UK GDPR) is a regulation in UK law on data protection and privacy in the European Union and the European Economic Area. It also applies to organisations outside the EU that process personal data of individuals in the EU.

    Principles considered:

    - Lawfulness, Fairness and Transparency
    - Purpose Limitation
    - Data Minimisation
    - Accuracy
    - Integrity and Confidentiality
    - Accountability

    ## Data Privacy

    The dataset contains no personally identifiable information and follows UK GDPR principles of data minimisation and purpose limitation.

    ## Bias

    Potential sampling and historical bias
    may exist within the dataset.

    ## Responsible AI

    Machine learning outputs should support
    decision-making and not replace human judgement.
    """)
    # add footer at the bottom of the page
    st.divider()

    st.caption(
        "Healthcare Insurance Cost Analysis Dashboard | Code Institute Capstone Project"
    )

# Create Business Requirement Validation page:
elif page == "Business Requirement Validation":

    st.title("Business Requirement Validation")

    st.write("""
    This section evaluates whether the project's
    original business requirements were successfully achieved.
    """)
# business requirement 1 validation section
    st.header("Business Requirement 1")
    st.subheader(
        "Identify the factors affecting healthcare insurance costs."
    )

# Add a Visual Validation Chart
    validation_df = pd.DataFrame({
        "Factor": [
            "Smoking Status",
            "BMI",
            "Age",
            "Region",
            "Sex"
        ],
        "Score": [
            5,
            4,
            4,
            2,
            1
        ]
    })

    fig = px.bar(
        validation_df,
        x="Factor",
        y="Score",
        color="Factor",
        title="Relative Impact on Insurance Charges"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    #---------------------------------------------------
# business requirement 1 validation summary
    st.info("""
    Business Requirement 1 Summary

    Smoking Status, BMI and Age were consistently identified
    as the strongest cost drivers through statistical testing,
    dashboard analysis and machine learning models.
    """)

    st.success("Requirement Achieved ✅")

    st.markdown("""
    ### Evidence

    The project successfully identified the main
    drivers of insurance costs using:

    - Exploratory Data Analysis
    - Statistical Testing
    - Correlation Analysis
    - Machine Learning

    ### Key Findings

    - Smoking Status is the strongest predictor.
    - BMI significantly affects healthcare costs.
    - Age significantly affects healthcare costs.
    - Region has a smaller but significant effect.
    - Sex has minimal influence.
    """)

    validation_df = pd.DataFrame({
        "Factor": [
            "Smoking Status",
            "BMI",
            "Age",
            "Region",
            "Sex"
        ],
        "Impact": [
            "Very High",
            "High",
            "High",
            "Moderate",
            "Low"
        ]
    })
    st.dataframe(validation_df)
    st.info("""
        Validation Summary

        The combination of exploratory data analysis,
        hypothesis testing and machine learning consistently
        identified Smoking Status, BMI and Age as the primary
        drivers of healthcare insurance costs.

        Business Requirement 1 was successfully achieved.
        """)

  # business requirement 2 validation section  
    st.header("Business Requirement 2")

    st.subheader(
        "Develop an interactive business intelligence dashboard."
    )
    #  Dashboard Deliverables Section
    st.subheader("Dashboard Deliverables")
   
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Power BI Dashboard", "Completed")

    with col2:
        st.metric("Streamlit Dashboard", "Completed")

    with col3:
        st.metric("Business Requirements", "2/2")

    st.success("Requirement Achieved ✅")
  
  #Dashboard evidence section

    st.subheader("Dashboard Evidence")
    st.subheader("Dashboard Deliverables")

    deliverables = pd.DataFrame({
        "Component": [
            "Power BI Dashboard",
            "Streamlit Dashboard",
            "Interactive Filters",
            "Machine Learning Results",
            "Business Recommendations"
        ],
        "Status": [
            "Completed",
            "Completed",
            "Completed",
            "Completed",
            "Completed"
        ]
    })

    st.dataframe(
        deliverables,
        use_container_width=True
    )

#---------------------------------------------------
    st.markdown("""
    ### Evidence
    Interactive dashboards were successfully developed using:

    - Power BI
    - Streamlit

    """)


    st.image(
        "docs/images/dashboard_screenshot.png",
        caption="Power BI Healthcare Insurance Cost Analysis Dashboard"
    )
    st.markdown("""
    ### Features Delivered

    - Interactive filters
    - KPI cards
    - Distribution analysis
    - Region comparison
    - Smoking analysis
    - Hypothesis validation
    - Machine learning evaluation
    - Ethical and governance reporting
    """)

    st.info("""
    Final Outcome

    Both business requirements were successfully
    achieved through statistical analysis,
    machine learning and interactive dashboard
    development.
    """)

    #hypothesis outcomes
    st.subheader("Hypothesis Validation Summary")
    hypothesis_df = pd.DataFrame({
        "Hypothesis":[
            "H1 Smoking",
            "H2 BMI",
            "H3 Children",
            "H4 Age",
            "H5 Region",
            "H6 Sex"
        ],
        "Result":[
            "Supported",
            "Supported",
            "Partially Supported",
            "Supported",
            "Supported",
            "Not Strongly Supported"
        ]
    })
    st.dataframe(hypothesis_df)

    st.success("""
    Final Assessment

    Both business requirements were fully achieved.

    The project successfully identified the primary drivers
    of healthcare insurance costs and delivered interactive
    business intelligence dashboards that support evidence-based
    decision making.
    """)
 
    # add footer at the bottom of the page
    st.divider()

    st.caption(
        "Healthcare Insurance Cost Analysis Dashboard | Code Institute Capstone Project"
    )

# Create Business Recommendations page:

elif page == "Business Recommendations":

    st.title("Business Recommendations")

    st.success("""
    Recommendation 1

    Smoking cessation programmes should be encouraged because smoking status was identified as the strongest predictor of healthcare insurance costs.
    """)

    st.success("""
    Recommendation 2

    Organisations should invest in wellness and BMI management initiatives to help reduce long-term healthcare expenditure.
    """)

    st.success("""
    Recommendation 3

    Age and BMI should be considered when designing personalised healthcare plans and preventive health interventions.
    """)

    st.success("""
    Recommendation 4

    Future analysis should include additional variables such as medical history, income and chronic conditions to improve model accuracy.
    """)
    # add footer at the bottom of the page
    st.divider()

    st.caption(
        "Healthcare Insurance Cost Analysis Dashboard | Code Institute Capstone Project"
    )


# Create Project Conclusions page:
elif page == "Project Conclusions":

    st.title("Project Conclusions")

    st.markdown("""
    ## Key Findings

    - Smoking status is the strongest predictor of healthcare insurance charges.
    - BMI and Age significantly influence costs.
    - Geographic region has a smaller but statistically significant impact.
    - Sex has limited influence on healthcare insurance charges.

    ## Best Machine Learning Model

    Random Forest Regression

    - R² = 0.8862
    - MAE = 2510.28
    - RMSE = 4572.72

    ## Project Outcome

    The dashboard successfully fulfils the business requirements by identifying key cost drivers and providing interactive visualisations to support data-driven decision making.
    """)
    # add footer at the bottom of the page
    st.divider()

    st.caption(
        "Healthcare Insurance Cost Analysis Dashboard | Code Institute Capstone Project"
    )

# Create Executive Summary page:

elif page == "Executive Summary":

    st.title("Executive Summary")

    st.markdown("""
    ## Key Findings
    - Smoking Status is the strongest predictor.
    - BMI significantly affects charges.
    - Age significantly affects charges.
    - Region has a modest effect.
    - Sex has limited impact.
    """)
    st.success("""
    ## Best Model

    Random Forest Regression

    R² = 0.8862
    MAE = 2510.28
    RMSE = 4572.72

    The Random Forest model achieved the highest predictive accuracy and provided feature importance
    rankings that aligned closely with statistical analysis and business findings.
    """)

    st.info("""
    ## Business Outcome
       The project successfully identified the key drivers of healthcare insurance costs
       and delivered interactive business intelligence dashboards to support evidence-based decision making.
    """)

    st.success("""
        Project Achievements

        ✅ Business Requirement 1 Successfully Achieved

        ✅ Business Requirement 2 Successfully Achieved

        ✅ Statistical Hypotheses Validated

        ✅ Interactive Power BI Dashboard Developed

        ✅ Interactive Streamlit Dashboard Developed

        ✅ Machine Learning Models Evaluated

        ✅ Ethical, Privacy and Governance Considerations Addressed
    """)

    # add footer at the bottom of the page
    st.divider()
    
    st.caption(
            "Healthcare Insurance Cost Analysis Dashboard | Code Institute Capstone Project"
        )
    