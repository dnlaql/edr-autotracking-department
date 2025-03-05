import streamlit as st
import pandas as pd
from modules.data_loader import load_edr_data
from modules.data_cleaning import clean_and_assign_department
from modules.eda import plot_threats_by_department, plot_time_series, plot_status_pie, plot_engine_effectiveness
from modules.filters import sidebar_filters

st.set_page_config(page_title="EDR Threat Analysis", layout="wide")
st.title("🛡️ EDR Auto-Tracking & Threat Analysis")

st.markdown("""
### 🚀 **Real-time Insights into Endpoint Detection & Response (EDR) Threats**
The **EDR Auto-Tracking & Threat Analysis Dashboard** helps IT security teams monitor incidents, detect patterns, and analyze security engine effectiveness.

🔹 **Upload your EDR datasets** (multiple CSVs supported)  
🔹 **Apply filters to refine threat insights**  
🔹 **Visualize trends, impacted departments & antivirus effectiveness**  
### _________________________________________________________________________________________________________________________________________________
""")

st.sidebar.header("📤 Upload Your Datasets")
uploaded_files = st.sidebar.file_uploader("Upload one or more CSV files", type=["csv"], accept_multiple_files=True)

if uploaded_files:
    dfs = [load_edr_data(file) for file in uploaded_files]  # Load each CSV into a DataFrame
    df = pd.concat(dfs, ignore_index=True)  # Merge all DataFrames into one
    
    df = clean_and_assign_department(df)  # Data Cleaning
    
    if df.empty or df.isnull().all().all():
        st.error("⚠️ The uploaded dataset is empty or contains only null values. Please upload valid CSV files.")
    else:
        sidebar_filters(df)
        
        # Ensure datetime format is correct
        df['Time Detected'] = pd.to_datetime(df['Time Detected'], errors='coerce')
        df.dropna(subset=['Time Detected'], inplace=True)
        
        # Apply filters
        if 'date_range' in st.session_state and st.session_state['date_range']:
            start_date, end_date = st.session_state['date_range']
            df = df[(df['Time Detected'] >= pd.Timestamp(start_date)) & (df['Time Detected'] <= pd.Timestamp(end_date))]
        
        if 'department' in st.session_state and st.session_state['department'] != 'All':
            df = df[df['Department'] == st.session_state['department']]
        
        if 'type_filter' in st.session_state and st.session_state['type_filter']:
            df = df[df['Type'].isin(st.session_state['type_filter'])]

        if 'status_filter' in st.session_state and st.session_state['status_filter']:
            df = df[df['Status'].isin(st.session_state['status_filter'])]
        
        if 'engine_filter' in st.session_state and st.session_state['engine_filter']:
            df = df[df['Engine'].isin(st.session_state['engine_filter'])]
        
        # Visualizations
        plot_threats_by_department(df)
        plot_time_series(df)
        plot_status_pie(df)
        plot_engine_effectiveness(df)
        
        st.subheader("📝 Filtered Data Table")
        st.dataframe(df)
else:
    st.warning("🚀 Please upload one or more CSV files to proceed!")
