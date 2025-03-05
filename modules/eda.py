import pandas as pd

def get_data_overview(df):
    """Return an overview of missing values and basic stats."""
    return {
        "Missing Values": df.isnull().sum(),
        "Data Types": df.dtypes
    }
