from flask import Flask

app = Flask(_name_)

@app.route("/")
def home():
    return "Hello Selva! Welcome to my Python Web Application."

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=10000)
