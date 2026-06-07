import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Predictive Maintenance Dashboard",
    layout="wide"
)

st.title("Predictive Maintenance & Fault Detection")

# Load data
comparison = pd.read_csv(
    "outputs/metrics/model_comparison.csv"
)

lead_times = pd.read_csv(
    "outputs/metrics/lead_times.csv"
)

st.header("Model Comparison")

st.dataframe(comparison)

st.header("Lead Time Statistics")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Mean Lead Time",
    round(lead_times["lead_time"].mean(), 2)
)

col2.metric(
    "Median Lead Time",
    round(lead_times["lead_time"].median(), 2)
)

col3.metric(
    "Maximum Lead Time",
    round(lead_times["lead_time"].max(), 2)
)

st.header("Lead Time Distribution")

fig, ax = plt.subplots(figsize=(8,4))

ax.hist(
    lead_times["lead_time"],
    bins=15
)

ax.set_xlabel("Lead Time")
ax.set_ylabel("Count")

st.pyplot(fig)

st.success("Dashboard Loaded Successfully") 
