import pandas as pd
import streamlit as st

# URL of the IP Mapping Dataset (stored in GitHub)
IP_MAPPING_URL = "https://raw.githubusercontent.com/dnlaql/edr-autotracking-department/refs/heads/main/data/ipmapping.csv"

@st.cache_data
def load_ip_mapping():
    """Load the IP mapping data from GitHub."""
    return pd.read_csv(IP_MAPPING_URL)

def load_edr_data(uploaded_file):
    """Load EDR Threat data from uploaded CSV file."""
    return pd.read_csv(uploaded_file)

