import streamlit as st

def initialize_filters():
    """Initialize or reset session state variables for filters."""
    st.session_state['date_range'] = []
    st.session_state['department'] = 'All'
    st.session_state['type_filter'] = []
    st.session_state['status_filter'] = []
    st.session_state['engine_filter'] = []

def sidebar_filters(df):
    """Sidebar UI elements for filtering."""
    st.sidebar.header("🎚️ Filters")

    # Date Range Filter
    st.session_state['date_range'] = st.sidebar.date_input("📅 Date Range", value=[])

    # Department Filter
    department_options = ['All'] + sorted(df['Department'].unique())
    st.session_state['department'] = st.sidebar.selectbox("🏢 Department", department_options)

    # Type Filter
    st.session_state['type_filter'] = st.sidebar.multiselect("🚨 Type", options=sorted(df['Type'].unique()))

    # Status Filter
    st.session_state['status_filter'] = st.sidebar.multiselect("📊 Status", options=sorted(df['Status'].unique()))

    # Engine Filter
    st.session_state['engine_filter'] = st.sidebar.multiselect("🖥️ Engine", options=sorted(df['Engine'].unique()))

    # Reset Filters Button
    if st.sidebar.button("🔄 Reset Filters"):
        initialize_filters()
