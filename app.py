from flask import Flask

app = Flask(_name_)

@app.route("/")
def home():
    return "Hello Rajathi! Welcome to my Python Web Application."
