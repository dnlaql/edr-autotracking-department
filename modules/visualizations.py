import plotly.express as px
import streamlit as st

def plot_threat_types_by_department(df):
    """Plot bar chart for threat types by department."""
    fig = px.bar(df, x='Department', y='Type', title="Threat Types by Department")
    st.plotly_chart(fig, use_container_width=True)

def plot_threat_timeline(df):
    """Plot time series of threats detected."""
    fig = px.line(df.groupby(df['Time Detected'].dt.date).size(), title='Daily Threats')
    st.plotly_chart(fig, use_container_width=True)

def plot_status_pie_chart(df):
    """Plot pie chart for threat resolution status."""
    status_counts = df['Status'].value_counts().reset_index()
    status_counts.columns = ['Status', 'Count']
    fig = px.pie(status_counts, values='Count', names='Status', title='Threat Resolution Status')
    st.plotly_chart(fig, use_container_width=True)

def plot_engine_effectiveness(df):
    """Plot antivirus engine effectiveness."""
    engine_status = df.groupby(['Engine', 'Status']).size().unstack().fillna(0)
    fig = px.bar(engine_status, barmode='group', title='Engine Effectiveness by Status')
    st.plotly_chart(fig, use_container_width=True)
