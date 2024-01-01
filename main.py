from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Happy New Year ! <h1>2024</h1>"

if __name__ == "__main__":
    app.run()
