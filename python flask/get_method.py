from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("form_get.html")


@app.route("/hello")
def hello():
    name = request.args.get("name")

    # This verifies what is inside my name variable it will be displayed in command line
    print(f"I found {name}")
    return f"Hello, {name}"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
