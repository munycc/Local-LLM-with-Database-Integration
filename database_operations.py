# database_operations.py

import sqlite3
import streamlit as st

@st.cache_data
def get_material_properties(material_name, property_type):
    table_name = f"{material_name} {property_type}"
    
    # Define the column name based on the property type
    property_columns = {
        'mechanical': 'Mechanical Properties',
        'thermal': 'Thermal Properties',
        'physical': 'Physical Properties'
    }
    
    property_column = property_columns.get(property_type.lower(), 'Properties')

    conn = sqlite3.connect('data/Materials.db')
    cursor = conn.cursor()
    
    query = f"""
    SELECT "{property_column}", Metric, English, Comments
    FROM "{table_name}"
    """
    
    cursor.execute(query)
    properties = cursor.fetchall()
    
    conn.close()
    return properties
