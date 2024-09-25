from flask import Flask, render_template, request
import prediction_module as c

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():
    predi = None
    perci= None  # Define a default value for predi
    d= None
    if request.method == "POST":
        name = request.form['username']
        predi, perci, d = c.prediction(name)
    return render_template("front.html", mine=predi, percentage=perci, details=d)


if __name__ == "__main__":
    app.run(debug=True)
