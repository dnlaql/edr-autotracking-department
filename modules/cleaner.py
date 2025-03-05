import pandas as pd
import ipaddress

def find_vlan_name(ip_address, ip_mapping_df):
    """Find VLAN name based on IP address using the provided mapping DataFrame."""
    try:
        ip = ipaddress.ip_address(ip_address)
        for _, row in ip_mapping_df.iterrows():
            if ip in ipaddress.ip_network(row['iprange']):
                return row['vlanname']
    except ValueError:
        return "Invalid IP"
    return "No VLAN found"

def clean_and_assign_department(edr_df, ip_mapping_df):
    """Clean the EDR data and assign departments based on IP mapping."""
    if 'IP Address' in edr_df.columns:
        edr_df['Department'] = edr_df['IP Address'].apply(lambda ip: find_vlan_name(ip, ip_mapping_df))
    return edr_df
