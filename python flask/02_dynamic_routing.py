from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome on root default domain"


@app.route("/blog/<blogger_name>")
def blog(blogger_name):
    return f"Welcome on the blog page of {blogger_name}"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
