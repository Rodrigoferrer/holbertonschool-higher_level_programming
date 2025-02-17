#!/usr/bin/python3
"""Module that defines a Student class"""


class Student:
    """Class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance
        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student
        Args:
            attrs (list): Optional list of attribute names to retrieve
        Returns:
            dict: Dictionary representation of the requested attributes"""

        if attrs is None:
            return self.__dict__

        my_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                my_dict[attr] = getattr(self, attr)
        return my_dict

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance
        Args:
            json (dict): Dictionary of attributes to replace."""

        for key, value in json.items():
            setattr(self, key, value)
