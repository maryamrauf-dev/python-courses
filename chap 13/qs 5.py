from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!\nThis is maryam 1st web. \nSo excited to share this with you.\n\tThank you</p>"

app.run()