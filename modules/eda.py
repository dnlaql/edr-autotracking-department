import streamlit as st
import plotly.express as px
import pandas as pd

def plot_threats_by_department(df):
    """📊 Plot threat distribution by department."""
    st.markdown("### 📊 Threats by Department")
    st.write(
        "This visualization provides a breakdown of threats detected across various departments within the organization. "
        "By analyzing this data, security teams can pinpoint which departments are most frequently targeted by cyber threats. "
        "Understanding this distribution allows organizations to allocate resources effectively, strengthen security measures, "
        "and implement targeted training programs for employees in high-risk departments."
    )

    if df.empty:
        st.warning("⚠️ No data available for visualization!")
        return

    fig = px.bar(df, x='Department', y='Type', title="Threat Types by Department")
    st.plotly_chart(fig, use_container_width=True)

def plot_time_series(df):
    """⏳ Plot daily threat trends over time."""
    st.markdown("### ⏳ Time Series of Threat Detection")
    st.write(
        "This time-series chart illustrates the daily frequency of detected threats over a given period. "
        "By analyzing trends and fluctuations, security analysts can identify peak periods of cyber activity, "
        "potential attack patterns, and anomalies that may require further investigation. "
        "Monitoring these trends helps in proactive threat mitigation and improving overall cybersecurity posture."
    )

    if df.empty:
        st.warning("⚠️ No data available for visualization!")
        return

    df['Time Detected'] = pd.to_datetime(df['Time Detected'], errors='coerce')
    daily_counts = df.groupby(df['Time Detected'].dt.date).size().reset_index(name='Count')

    fig = px.line(daily_counts, x='Time Detected', y='Count', title="Daily Threats Detected")
    st.plotly_chart(fig, use_container_width=True)

def plot_status_pie(df):
    """📈 Plot threat resolution status distribution."""
    st.markdown("### 📈 Status of Threat Resolutions")
    st.write(
        "This pie chart provides an overview of the resolution status of detected threats within the system. "
        "It categorizes threats based on whether they have been successfully resolved, are currently in progress, "
        "or remain unresolved. Understanding the distribution of threat resolutions helps assess the efficiency of "
        "the security response team, identify potential backlog issues, and ensure timely remediation of critical threats."
    )

    if df.empty:
        st.warning("⚠️ No data available for visualization!")
        return

    status_counts = df['Status'].value_counts().reset_index()
    status_counts.columns = ['Status', 'Count']

    fig = px.pie(status_counts, values='Count', names='Status', title='Threat Resolution Status')
    st.plotly_chart(fig, use_container_width=True)

def plot_engine_effectiveness(df):
    """🖥️ Plot antivirus engine effectiveness in detecting and resolving threats."""
    st.markdown("### 🖥️ Antivirus Engine Effectiveness")
    st.write(
        "This bar chart compares the effectiveness of different antivirus engines in detecting and resolving threats. "
        "Each security engine's performance is evaluated based on the number of detected threats and their resolution status. "
        "By analyzing this data, security teams can determine which antivirus solutions are the most reliable, "
        "identify potential gaps in protection, and make informed decisions about upgrading or fine-tuning security tools."
    )

    if df.empty:
        st.warning("⚠️ No data available for visualization!")
        return

    engine_status = df.groupby(['Engine', 'Status']).size().unstack().fillna(0)

    fig = px.bar(engine_status, barmode='group', title='Engine Effectiveness by Status')
    st.plotly_chart(fig, use_container_width=True)
