import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="🚦 Road Accident Master Dashboard", layout="wide")

# Load dataset
df = pd.read_csv("accident_prediction_india.csv")

st.title("🚗 Master-Level Road Accident Analytics Dashboard")

# Sidebar filters
with st.sidebar:
    st.header("🔍 Filters")
    years = st.multiselect("Select Year(s)", sorted(df["Year"].unique()), default=sorted(df["Year"].unique()))
    months = st.multiselect("Select Month(s)", sorted(df["Month"].unique()), default=sorted(df["Month"].unique()))
    states = st.multiselect("Select State(s)", sorted(df["State Name"].unique()), default=sorted(df["State Name"].unique()))

# Filter data
filtered_df = df[df["Year"].isin(years) & df["Month"].isin(months) & df["State Name"].isin(states)]

# Summary metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Accidents", len(filtered_df))
col2.metric("Total Casualties", filtered_df["Number of Casualties"].sum())
col3.metric("Total Fatalities", filtered_df["Number of Fatalities"].sum())
col4.metric("Avg Driver Age", round(filtered_df["Driver Age"].mean(), 1))

# Accident Severity Pie
st.subheader("📌 Accident Severity Distribution")
fig1 = px.pie(filtered_df, names="Accident Severity", title="Accident Severity Distribution")
st.plotly_chart(fig1, use_container_width=True)

# Accidents by State
st.subheader("🗺️ Accidents by State")
state_count = filtered_df["State Name"].value_counts().reset_index()
state_count.columns = ["State", "Accident Count"]
fig2 = px.bar(state_count, x="State", y="Accident Count", color="Accident Count", title="Accidents by State")
st.plotly_chart(fig2, use_container_width=True)

# Heatmap of Time vs Severity
if "Time of Day" in df.columns:
    st.subheader("⏱️ Time of Day vs. Accident Severity")
    pivot = pd.crosstab(filtered_df["Time of Day"], filtered_df["Accident Severity"])
    fig3, ax3 = plt.subplots(figsize=(10, 4))
    sns.heatmap(pivot, annot=True, cmap="YlGnBu", fmt="d", ax=ax3)
    st.pyplot(fig3)

# Alcohol Involvement
if "Alcohol Involvement" in df.columns:
    st.subheader("🍺 Alcohol Involvement")
    alcohol_count = filtered_df["Alcohol Involvement"].value_counts().reset_index()
    alcohol_count.columns = ["Alcohol", "Count"]
    fig4 = px.bar(alcohol_count, x="Alcohol", y="Count", color="Alcohol", title="Alcohol Involvement in Accidents")
    st.plotly_chart(fig4, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("🚀 Built by **Sudheesh** for AI & DS Internship - Master Level Project")
