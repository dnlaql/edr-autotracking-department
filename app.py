import streamlit as st
import pandas as pd
from modules.data_loader import load_edr_data
from modules.data_cleaning import clean_and_assign_department
from modules.eda import plot_threats_by_department, plot_time_series, plot_status_pie, plot_engine_effectiveness
from modules.filters import sidebar_filters
from modules.chatbot import chatbot_response  # Import chatbot function

# Title
st.title("🛡️ EDR Auto-Tracking & Threat Analysis")

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

    # Chatbot Section
    st.subheader("💬 Chatbot: Ask About Threat Insights")

    if st.button("Enable Chatbot 🤖"):
        user_input = st.text_input("Type your question here:")
        if user_input:
            eda_results = {
                "most_affected_department": df["Department"].value_counts().idxmax(),
                "most_common_threat": df["Type"].value_counts().idxmax(),
                "resolved_threats_count": df[df["Status"] == "Resolved"].shape[0],
                "total_threats_count": len(df)
            }
            response = chatbot_response(user_input, eda_results)
            st.write(f"💬 **Chatbot:** {response}")

else:
    st.warning("🚀 Please upload a CSV file to proceed!")
