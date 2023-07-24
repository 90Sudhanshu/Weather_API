from flask import Flask, render_template

app = Flask("Web")


@app.route('/home')
def home():
    # return render_template("/index.html")
    return render_template("index.html")


@app.route('/intro')
def intro():
    return render_template("intro.html")


@app.route('/cartoons')
def cartoons():
    return render_template("cartoons.html")


@app.route('/AI')
def ai():
    return render_template("AI.html")


app.run(debug=True)