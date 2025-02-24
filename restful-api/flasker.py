#!/usr/bin/python3


from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    user = input("Cual es tu nombre")
    return user

if __name__ == "__main__": app.run()