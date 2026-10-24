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
        "Ethics"
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

# Create Machine Learning page:
elif page == "Machine Learning":

    st.title("Machine Learning Results")

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

# Create Ethics page:

elif page == "Ethics":

    st.title("Ethics, Privacy and Governance")

    st.markdown("""
    ## UK GDPR

    Principles considered:

    - Lawfulness, Fairness and Transparency
    - Purpose Limitation
    - Data Minimisation
    - Accuracy
    - Integrity and Confidentiality
    - Accountability

    ## Data Privacy

    The dataset contains no personally identifiable information.

    ## Bias

    Potential sampling and historical bias
    may exist within the dataset.

    ## Responsible AI

    Machine learning outputs should support
    decision-making and not replace human judgement.
    """)