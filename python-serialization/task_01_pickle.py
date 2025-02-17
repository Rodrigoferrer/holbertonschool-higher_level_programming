#!/usr/bin/python3
"""Module for custom object serialization using pickle"""


import pickle


class CustomObject:
   """Class that defines a custom object with pickle serialization"""

   def __init__(self, name, age, is_student):
       """Initialize CustomObject with name, age and student status
       
       Args:
           name (str): The name of the person
           age (int): The age of the person
           is_student (bool): Whether the person is a student"""
       
       self.name = name
       self.age = age 
       self.is_student = is_student

   def display(self):
       """Display the object's attributes in formatted output"""
       
       print(f"Name: {self.name}")
       print(f"Age: {self.age}")
       print(f"Is Student: {self.is_student}")

   def serialize(self, filename):
       """Serialize the object to a file using pickle
       
       Args:
           filename (str): Name of file to save serialized object
           
       Returns:
           None if error occurs during serialization"""
       
       try:
           with open(filename, 'wb') as f:
               pickle.dump(self, f)
       except Exception:
           return None

   @classmethod
   def deserialize(cls, filename):
       """Deserialize and return object from a file
       
       Args:
           filename (str): Name of file containing serialized object
           
       Returns:
           CustomObject instance or None if error occurs"""
       
       try:
           with open(filename, 'rb') as f:
               return pickle.load(f)
       except Exception:
           return None
