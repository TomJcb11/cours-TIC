from flask import Flask

app = Flask(__name__)


@app.route("/")
def root_message():
    return "Welcome on root default domain"


@app.route("/hello")
def hello_message():
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True, port=5000, use_reloader=True)
