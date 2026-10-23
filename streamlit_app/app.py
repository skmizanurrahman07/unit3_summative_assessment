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

    st.title("Healthcare Insurance Cost Analysis")

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

# ---------------------------------------------------
# Sidebar Filters by Region and Smoking Status
# ---------------------------------------------------

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

# Create new Filtered DataFrame

filtered_df = df[
    (df["Region"].isin(selected_region))
    &
    (df["Smoker"].isin(selected_smoker))
]
# ---------------------------------------------------
# Dataset Preview
# ---------------------------------------------------
st.subheader("Dataset Preview")
st.dataframe(filtered_df)

# ---------------------------------------------------
# KPI Dashboard
#---------------------------------------------------
st.subheader("Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(
        label="Average Charge",
        value=f"${filtered_df['Charges'].mean():,.0f}"
    )

with col2:
    st.metric(
        label="Average BMI",
        value=f"{filtered_df['BMI'].mean():.1f}"
    )

with col3:
    st.metric(
        label="Average Age",
        value=f"{filtered_df['Age'].mean():.1f}"
    )

with col4:
    st.metric(
        label="Policyholders",
        value=f"{len(filtered_df):,}"
    )
# ---------------------------------------------------
# Insurance Charge Distribution Histogram
# ---------------------------------------------------
st.subheader("Insurance Charge Distribution")

fig = px.histogram(
    filtered_df,
    x="Charges",
    color="Smoker",
    nbins=30,
    barmode="overlay",
    opacity=0.7,
    title="Distribution of Insurance Charges"
)

fig.update_layout(
    xaxis_title="Insurance Charges ($)",
    yaxis_title="Count",
    legend_title="Smoker"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
# BMI vs Charges Scatter Plot
# ---------------------------------------------------
# BMI vs Charges
# ---------------------------------------------------
col_left, col_right = st.columns(2)
with col_left:

    st.subheader("BMI vs Insurance Charges")
    scatter_fig = px.scatter(
        filtered_df,
        x="BMI",
        y="Charges",
        color="Smoker",
        size="Age",
        hover_data=["Region", "Children"],
        title="BMI vs Insurance Charges"
    )

    scatter_fig.update_layout(
        xaxis_title="BMI",
        yaxis_title="Insurance Charges ($)"
    )

    st.plotly_chart(
        scatter_fig,
        use_container_width=True
    )
# Region Comparison Chart
# ---------------------------------------------------
# Average Charges by Region
# ---------------------------------------------------
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
        title="Average Insurance Charges by Region"
    )

    st.plotly_chart(
        region_fig,
        use_container_width=True
    )

# Smoker Breakdown
# ---------------------------------------------------
# Smoker Distribution
# ---------------------------------------------------

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