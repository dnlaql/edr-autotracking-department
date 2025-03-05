import streamlit as st
import pandas as pd

def load_uploaded_file(uploaded_file):
    """Load and read CSV file into a DataFrame."""
    if uploaded_file is not None:
        return pd.read_csv(uploaded_file)
    return None

def load_ip_mapping(ip_file):
    """Load IP Mapping CSV file into a DataFrame."""
    if ip_file is not None:
        return pd.read_csv(ip_file)
    return None
