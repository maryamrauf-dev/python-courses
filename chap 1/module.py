from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():#just checking the multi cuser functionality of vs code
    return "Hello, Flask!"#just checking the multi cuser functionality of vs code

    app.run(debug=True)#just checking the multi cuser functionality of vs code
if __name__ == '__main__':#just checking the multi cuser functionality of vs code