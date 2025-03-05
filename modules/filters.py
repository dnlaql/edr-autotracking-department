import streamlit as st

def initialize_filters():
    """Initialize session state for filters."""
    if 'date_range' not in st.session_state:
        st.session_state['date_range'] = []
    if 'department' not in st.session_state:
        st.session_state['department'] = 'All'
    if 'type_filter' not in st.session_state:
        st.session_state['type_filter'] = []
    if 'status_filter' not in st.session_state:
        st.session_state['status_filter'] = []
    if 'engine_filter' not in st.session_state:
        st.session_state['engine_filter'] = []

def apply_filters(df):
    """Apply user-selected filters to the dataset."""
    filtered_data = df.copy()

    # Apply Date Range Filter
    if st.session_state['date_range']:
        start_date, end_date = st.session_state['date_range']
        filtered_data = filtered_data[
            (filtered_data['Time Detected'] >= pd.Timestamp(start_date)) &
            (filtered_data['Time Detected'] <= pd.Timestamp(end_date))
        ]

    # Apply Department Filter
    if st.session_state['department'] != 'All':
        filtered_data = filtered_data[filtered_data['Department'] == st.session_state['department']]

    # Apply Type Filter
    if st.session_state['type_filter']:
        filtered_data = filtered_data[filtered_data['Type'].isin(st.session_state['type_filter'])]

    # Apply Status Filter
    if st.session_state['status_filter']:
        filtered_data = filtered_data[filtered_data['Status'].isin(st.session_state['status_filter'])]

    # Apply Engine Filter
    if st.session_state['engine_filter']:
        filtered_data = filtered_data[filtered_data['Engine'].isin(st.session_state['engine_filter'])]

    return filtered_data
