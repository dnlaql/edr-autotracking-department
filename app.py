import streamlit as st
import pandas as pd
from modules.data_loader import load_edr_data
from modules.data_cleaning import clean_and_assign_department
from modules.eda import plot_threats_by_department, plot_time_series, plot_status_pie, plot_engine_effectiveness
from modules.filters import sidebar_filters

# 🎯 **Dashboard Title & Introduction**
st.set_page_config(page_title="EDR Threat Analysis", layout="wide")
st.title("🛡️ EDR Auto-Tracking & Threat Analysis")

st.markdown("""
### 🚀 **Real-time Insights into Endpoint Detection & Response (EDR) Threats**
The **EDR Auto-Tracking & Threat Analysis Dashboard** helps IT security teams monitor incidents, detect patterns, and analyze security engine effectiveness.

🔹 **Upload your EDR dataset**  
🔹 **Apply filters to refine threat insights**  
🔹 **Visualize trends, impacted departments & antivirus effectiveness**  
""")

# 📤 **File Upload Section**
st.sidebar.header("📤 Upload Your Dataset")
uploaded_file = st.sidebar.file_uploader("Upload EDR Threat Data (CSV)", type=["csv"])

if uploaded_file:
    # 🛠️ **Load & Clean Data**
    df = load_edr_data(uploaded_file)
    df = clean_and_assign_department(df)

    # 📌 **Check if Data is Valid**
    if df.empty:
        st.error("⚠️ The uploaded dataset is empty. Please upload a valid CSV file.")
    else:
        # 🔍 **Apply Sidebar Filters**
        sidebar_filters(df)

        # ✅ **Filter Data Based on Sidebar Selections**
        if 'date_range' in st.session_state and st.session_state['date_range']:
            start_date, end_date = st.session_state['date_range']
            df = df[(df['Time Detected'] >= pd.Timestamp(start_date)) & 
                    (df['Time Detected'] <= pd.Timestamp(end_date))]

        if 'department' in st.session_state and st.session_state['department'] != 'All':
            df = df[df['Department'] == st.session_state['department']]

        if 'type_filter' in st.session_state and st.session_state['type_filter']:
            df = df[df['Type'].isin(st.session_state['type_filter'])]

        if 'status_filter' in st.session_state and st.session_state['status_filter']:
            df = df[df['Status'].isin(st.session_state['status_filter'])]

        if 'engine_filter' in st.session_state and st.session_state['engine_filter']:
            df = df[df['Engine'].isin(st.session_state['engine_filter'])]

        # 📌 **EDA Section Description**
        st.markdown("""
        ## 📊 Exploratory Data Analysis (EDA)
        Below are key insights generated from your dataset:
        - **Threats by Department:** Identify which departments face the highest cybersecurity threats.
        - **Time Series Analysis:** Detect trends over time to analyze peak attack periods.
        - **Threat Resolution Status:** Monitor how many threats are resolved or pending action.
        - **Antivirus Engine Effectiveness:** Assess how well different antivirus engines handle threats.
        """)

        # 🔥 **Display Visualizations**
        if not df.empty:
            plot_threats_by_department(df)
            plot_time_series(df)
            plot_status_pie(df)
            plot_engine_effectiveness(df)
        else:
            st.warning("⚠️ No matching data found after applying filters!")

        # 📊 **Display Filtered Data Table**
        st.subheader("📝 Filtered Data Table")
        st.dataframe(df)

else:
    st.warning("🚀 Please upload a CSV file to proceed!")
