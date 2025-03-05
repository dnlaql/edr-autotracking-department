import streamlit as st
import pandas as pd
from modules.data_loader import load_uploaded_file, load_ip_mapping
from modules.cleaner import clean_and_assign_department
from modules.filters import initialize_filters, apply_filters
from modules.eda import get_data_overview
from modules.visualizations import plot_threat_types_by_department, plot_threat_timeline, plot_status_pie_chart, plot_engine_effectiveness

# Initialize session state
initialize_filters()

# Sidebar: File Upload
st.sidebar.header('Upload Files 📂')
edr_file = st.sidebar.file_uploader("Upload EDR Threat CSV", type=['csv'])
ip_mapping_file = st.sidebar.file_uploader("Upload IP Mapping CSV", type=['csv'])

if edr_file and ip_mapping_file:
    df = load_uploaded_file(edr_file)
    ip_mapping_df = load_ip_mapping(ip_mapping_file)

    # Clean and assign departments
    df = clean_and_assign_department(df, ip_mapping_df)

    # Convert 'Time Detected' column to datetime
    df['Time Detected'] = pd.to_datetime(df['Time Detected'])

    # Apply filters
    filtered_df = apply_filters(df)

    # Title & Introduction
    st.title('Threat Monitoring & Analysis Dashboard 🛡️')

    # Data Overview
    st.subheader("Data Overview 📊")
    overview = get_data_overview(filtered_df)
    st.write(overview)

    # Visualizations
    st.subheader("Threat Distribution by Department")
    plot_threat_types_by_department(filtered_df)

    st.subheader("Time Series Analysis of Threat Detection")
    plot_threat_timeline(filtered_df)

    st.subheader("Threat Resolution Status")
    plot_status_pie_chart(filtered_df)

    st.subheader("Antivirus Engine Effectiveness")
    plot_engine_effectiveness(filtered_df)

    # Display Table
    st.subheader("Filtered Data Table 📝")
    st.dataframe(filtered_df)

else:
    st.info("Please upload both EDR threat and IP mapping files to proceed.")
