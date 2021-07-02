from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, <b>Satyam!</b> <img src='https://thestoragess.blob.core.windows.net/testcon/PhotoGrid_1590937364961.jpg' width='100' height='200'/>"
