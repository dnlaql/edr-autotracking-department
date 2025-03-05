import pandas as pd
import ipaddress
from modules.data_loader import load_ip_mapping

def find_department(ip_address, ip_mapping_df):
    """Find VLAN (Department) based on IP Address."""
    try:
        ip = ipaddress.ip_address(ip_address)
        for _, row in ip_mapping_df.iterrows():
            if ip in ipaddress.ip_network(row['iprange']):
                return row['vlanname']
    except ValueError:
        return "Invalid IP"
    return "No VLAN Found"

def clean_and_assign_department(df):
    """Clean dataset and assign department to each entry."""
    ip_mapping_df = load_ip_mapping()
    df['Department'] = df['IP Address'].apply(lambda ip: find_department(ip, ip_mapping_df))
    df['Time Detected'] = pd.to_datetime(df['Time Detected'])  # Convert time column
    return df
