import streamlit as st
import plotly.express as px

def plot_threats_by_department(df):
    """Plot threat distribution by department."""
    st.subheader("📊 Threats by Department")
    fig = px.bar(df, x='Department', y='Type', title="Threat Types by Department")
    st.plotly_chart(fig, use_container_width=True)

def plot_time_series(df):
    """Plot daily threat trends."""
    st.subheader("⏳ Time Series of Threat Detection")
    daily_counts = df.groupby(df['Time Detected'].dt.date).size().reset_index(name='Count')
    fig = px.line(daily_counts, x='Time Detected', y='Count', title="Daily Threats Detected")
    st.plotly_chart(fig, use_container_width=True)

def plot_status_pie(df):
    """Plot status of threat resolutions."""
    st.subheader("📈 Status of Threat Resolutions")
    status_counts = df['Status'].value_counts().reset_index()
    status_counts.columns = ['Status', 'Count']
    fig = px.pie(status_counts, values='Count', names='Status', title='Threat Resolution Status')
    st.plotly_chart(fig, use_container_width=True)

def plot_engine_effectiveness(df):
    """Plot antivirus engine effectiveness."""
    st.subheader("🖥️ Antivirus Engine Effectiveness")
    engine_status = df.groupby(['Engine', 'Status']).size().unstack().fillna(0)
    fig = px.bar(engine_status, barmode='group', title='Engine Effectiveness by Status')
    st.plotly_chart(fig, use_container_width=True)
