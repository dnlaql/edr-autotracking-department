import streamlit as st
import plotly.express as px
import pandas as pd

"""
# 📊 EDA (Exploratory Data Analysis) Module

This module contains functions for visualizing EDR (Endpoint Detection & Response) threat data. 
It helps security teams analyze patterns, identify vulnerable departments, and assess security measures.

## 🔍 **Visualizations Included:**
- **Threats by Department**: Identify departments most affected by threats.
- **Time Series of Threats**: Track daily trends in threat detection.
- **Threat Resolution Status**: Analyze how threats are being resolved.
- **Antivirus Engine Effectiveness**: Evaluate performance of security solutions.
"""

def plot_threats_by_department(df):
    """
    📊 Plot threat distribution by department.

    This function generates a **bar chart** displaying the number of threats detected 
    in each department. It helps identify which departments are most affected 
    by cybersecurity threats.

    Parameters:
        df (DataFrame): The preprocessed EDR dataset containing department-wise threat data.
    """
    st.markdown("## 📊 Threats by Department")
    
    if df.empty:
        st.warning("⚠️ No data available for visualization!")
        return

    fig = px.bar(df, x='Department', y='Type', title="Threat Types by Department")
    st.plotly_chart(fig, use_container_width=True)

def plot_time_series(df):
    """
    ⏳ Plot daily threat trends over time.

    This function generates a **line chart** that visualizes the number of threats detected 
    each day. It provides insights into trends, helping security teams monitor periods 
    of increased threat activity.

    Parameters:
        df (DataFrame): The preprocessed EDR dataset with time-based threat data.
    """
    st.markdown("## ⏳ Time Series of Threat Detection")
    
    if df.empty:
        st.warning("⚠️ No data available for visualization!")
        return

    # Ensure 'Time Detected' is in datetime format
    df['Time Detected'] = pd.to_datetime(df['Time Detected'], errors='coerce')
    
    # Group by daily threat count
    daily_counts = df.groupby(df['Time Detected'].dt.date).size().reset_index(name='Count')

    fig = px.line(daily_counts, x='Time Detected', y='Count', title="Daily Threats Detected")
    st.plotly_chart(fig, use_container_width=True)

def plot_status_pie(df):
    """
    📈 Plot threat resolution status distribution.

    This function generates a **pie chart** that displays the distribution of 
    threat resolution statuses, such as "Resolved," "In Progress," or "Unresolved." 
    It helps in assessing the efficiency of incident response.

    Parameters:
        df (DataFrame): The preprocessed EDR dataset containing threat status information.
    """
    st.markdown("## 📈 Status of Threat Resolutions")

    if df.empty:
        st.warning("⚠️ No data available for visualization!")
        return

    status_counts = df['Status'].value_counts().reset_index()
    status_counts.columns = ['Status', 'Count']

    fig = px.pie(status_counts, values='Count', names='Status', title='Threat Resolution Status')
    st.plotly_chart(fig, use_container_width=True)

def plot_engine_effectiveness(df):
    """
    🖥️ Plot antivirus engine effectiveness in detecting and resolving threats.

    This function generates a **grouped bar chart** that compares the effectiveness 
    of different antivirus engines based on threat resolution status. 
    It helps in evaluating the performance of security solutions.

    Parameters:
        df (DataFrame): The preprocessed EDR dataset containing engine-wise threat status.
    """
    st.markdown("## 🖥️ Antivirus Engine Effectiveness")
    
    if df.empty:
        st.warning("⚠️ No data available for visualization!")
        return

    engine_status = df.groupby(['Engine', 'Status']).size().unstack().fillna(0)

    fig = px.bar(engine_status, barmode='group', title='Engine Effectiveness by Status')
    st.plotly_chart(fig, use_container_width=True)
