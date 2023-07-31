from flask import Flask, render_template

app = Flask("Web")

posts = [
    {
        'name': 'Ram',
        'blog': 'Blog 1',
        'date': '25-July-2023'
    },
    {
        'name': 'Krishna',
        'blog': 'Blog 2',
        'date': '25-July-2023'

    }
]


@app.route('/home')
def home():
    return render_template("index.html", posts=posts)


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