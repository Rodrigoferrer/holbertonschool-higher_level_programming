#!/usr/bin/python3
"""Module for converting CSV to JSON"""


import csv
import json


def convert_csv_to_json(csv_filename):
   """Convert CSV file to JSON
   
   Args:
       csv_filename (str): Name of input CSV file
       
   Returns:
       bool: True if conversion successful, False otherwise"""

   try:

       with open(csv_filename, 'r', encoding='utf-8') as csv_file:
           csv_data = csv.DictReader(csv_file)
           data_list = list(csv_data)


       with open('data.json', 'w', encoding='utf-8') as json_file:
           json.dump(data_list, json_file, indent=4)
           
       return True

   except Exception:
       return False