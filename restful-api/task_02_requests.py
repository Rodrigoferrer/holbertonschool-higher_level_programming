#!/usr/python3
"""Requests"""


import requests
import csv


def fetch_and_print_posts():
    """Function to retrieve posts from jsonplaceholder and print them"""
    
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print("{}["title"]".format(post))

def fetch_and_save_posts():
    """function to save posts from jsonplaceholder"""
    
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        data = []

        for post in posts:
            data.append({'id': post['id'], 'title': post['title'], 'body': post['body']})

        with open("posts.csv", "w") as file:
            writer = csv.DictWriter(file, fieldnames["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data)
