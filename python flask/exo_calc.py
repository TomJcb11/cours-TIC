from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("calculatrice.html")


@app.route("/calculer", methods=["POST"])
def calculer():
    num1 = float(request.form["num1"])
    num2 = float(request.form["num2"])
    operation = request.form["operation"]

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        result = num1 / num2 if num2 != 0 else -1

    else:
        result = "Invalid operation"

    return render_template("calculatrice_result.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
