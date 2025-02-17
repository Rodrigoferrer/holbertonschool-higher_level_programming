#!/usr/bin/python3
"""Module for basic dictionary serialization to JSON"""


import json


def serialize_and_save_to_file(data, filename):
    """Serialize dictionary to JSON and save to file
    
    Args:
        data (dict): Dictionary to serialize
        filename (str): Name of output JSON file
    """
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load and deserialize JSON file to dictionary
    
    Args:
        filename (str): Name of input JSON file
        
    Returns:
        dict: Deserialized dictionary from JSON file
    """
    
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
