import streamlit as st
import plotly.express as px
import pandas as pd

def plot_threats_by_department(df):
    """📊 Plot threat distribution by department."""
    st.markdown("### 📊 Threats by Department")
    st.write("This bar chart shows the number of threats detected in each department, helping identify the most vulnerable areas.")

    if df.empty:
        st.warning("⚠️ No data available for visualization!")
        return

    fig = px.bar(df, x='Department', y='Type', title="Threat Types by Department")
    st.plotly_chart(fig, use_container_width=True)

def plot_time_series(df):
    """⏳ Plot daily threat trends over time."""
    st.markdown("### ⏳ Time Series of Threat Detection")
    st.write("This line chart visualizes the number of threats detected per day, helping security teams monitor trends and spikes.")

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
    st.write("This pie chart displays the proportion of threats that have been resolved, are in progress, or remain unresolved.")

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
    st.write("This bar chart compares the performance of different antivirus engines, helping evaluate their effectiveness in handling threats.")

    if df.empty:
        st.warning("⚠️ No data available for visualization!")
        return

    engine_status = df.groupby(['Engine', 'Status']).size().unstack().fillna(0)

    fig = px.bar(engine_status, barmode='group', title='Engine Effectiveness by Status')
    st.plotly_chart(fig, use_container_width=True)
