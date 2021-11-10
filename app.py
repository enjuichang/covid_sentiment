from flask import Flask, render_template, request
from models import model

app = Flask(__name__)


@app.route("/", methods = ['GET','POST'])
def classify():
    if request.method == "POST":
        text = request.form['input']
        output = model.classify_model(text)

    return render_template("index.html", cat = output)

if __name__ == "__main__":
    app.run(debug=True)