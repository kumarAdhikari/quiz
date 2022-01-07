from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)
questions = {"What is capital of nepal?": "kathmandu", "What is capital of india?": "new delhi",
             "How many meter in kilometer?": "1000"}
@app.route("/")
def home():
    return render_template("index.html", content=questions)

if __name__ == "__main__":
    app.run(debug=True)
