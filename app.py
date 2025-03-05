import streamlit as st
import pandas as pd
from modules.data_loader import load_edr_data
from modules.data_cleaning import clean_and_assign_department
from modules.eda import plot_threats_by_department, plot_time_series, plot_status_pie, plot_engine_effectiveness
from modules.filters import sidebar_filters, initialize_filters

# Title
st.title("🛡️ EDR Auto-Tracking & Threat Analysis")
st.markdown("""
The **EDR Auto-Tracking & Threat Analysis Dashboard** provides real-time insights into endpoint detection and response (EDR) threats. 
Upload your EDR threat data to visualize incidents, monitor trends, and assess security engine effectiveness. 
Use the interactive filters to analyze threats by department, type, and status, helping IT security teams enhance their cybersecurity defenses. 🚀
""")

# Upload CSV File
st.sidebar.header("📤 Upload Your Dataset")
uploaded_file = st.sidebar.file_uploader("Upload EDR Threat Data (CSV)", type=["csv"])

if uploaded_file:
    df = load_edr_data(uploaded_file)
    df = clean_and_assign_department(df)

    # Sidebar Filters
    sidebar_filters(df)

    # Apply Filters
    if st.session_state['date_range']:
        start_date, end_date = st.session_state['date_range'][0], st.session_state['date_range'][1]
        df = df[(df['Time Detected'] >= pd.Timestamp(start_date)) & (df['Time Detected'] <= pd.Timestamp(end_date))]

    if st.session_state['department'] != 'All':
        df = df[df['Department'] == st.session_state['department']]

    if st.session_state['type_filter']:
        df = df[df['Type'].isin(st.session_state['type_filter'])]

    if st.session_state['status_filter']:
        df = df[df['Status'].isin(st.session_state['status_filter'])]

    if st.session_state['engine_filter']:
        df = df[df['Engine'].isin(st.session_state['engine_filter'])]

    # Display EDA
    plot_threats_by_department(df)
    plot_time_series(df)
    plot_status_pie(df)
    plot_engine_effectiveness(df)

    # Display Data Table
    st.subheader("📝 Filtered Data Table")
    st.dataframe(df)

else:
    st.warning("🚀 Please upload a CSV file to proceed!")
