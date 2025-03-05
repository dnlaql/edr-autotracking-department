import streamlit as st
import pandas as pd
from modules.data_loader import load_edr_data
from modules.data_cleaning import clean_and_assign_department
from modules.eda import plot_threats_by_department, plot_time_series, plot_status_pie, plot_engine_effectiveness
from modules.filters import sidebar_filters

# 🎯 **Dashboard Title & Introduction**
st.set_page_config(page_title="EDR Threat Analysis")  # Default layout (centered)
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

        # 🔥 **EDA Results with Descriptions**

        # 📊 **Threats by Department**
        st.markdown("""
        
        This chart shows the distribution of threats detected in different departments.  
        It helps identify which departments are most vulnerable to cyber threats.
        """)
        plot_threats_by_department(df)

         st.markdown("""
        This chart shows the distribution of threats detected in different departments.  
        It helps identify which departments are most vulnerable to cyber threats.
        """)

        # ⏳ **Time Series Analysis**
        st.markdown("""
        ### ⏳ Time Series Analysis
        This line chart visualizes daily trends in detected threats.  
        Helps in identifying peak attack periods and monitoring security incidents over time.
        """)
        plot_time_series(df)

        # 📈 **Threat Resolution Status**
        st.markdown("""
        ### 📈 Threat Resolution Status
        This pie chart shows how many threats are resolved, in progress, or still unresolved.  
        Useful for assessing the efficiency of the security response team.
        """)
        plot_status_pie(df)

        # 🖥️ **Antivirus Engine Effectiveness**
        st.markdown("""
        ### 🖥️ Antivirus Engine Effectiveness
        This bar chart compares the performance of different antivirus engines.  
        It helps evaluate which security tools are most effective in handling threats.
        """)
        plot_engine_effectiveness(df)

        # 📊 **Display Filtered Data Table**
        st.subheader("📝 Filtered Data Table")
        st.dataframe(df)

else:
    st.warning("🚀 Please upload a CSV file to proceed!")
