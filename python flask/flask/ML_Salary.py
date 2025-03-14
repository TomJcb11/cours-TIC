from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

model_path = "./model.pkl"
# Charger le modèle au démarrage du serveur
model = joblib.load(model_path)


@app.route("/")
def home():
    return render_template("salary_ML_predict.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        experience = float(
            request.form["experience"]
        )  # Récupérer l'expérience depuis le formulaire
        prediction = model.predict(np.array([[experience]]))
        formatted_salary = "{:,.2f}".format(prediction[0]).replace(",", " ")

        return render_template(
            "salary_ML_predict.html",
            prediction=formatted_salary,
            experience=experience,
        )

    except Exception as e:
        return render_template("index.html", error=str(e))


if __name__ == "__main__":
    app.run(debug=True)
