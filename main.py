from flask import Flask, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")



@app.route('/v1/<station>/<date>')
def about(station, date):
    filename = 'data-small\TG_STAID' + str(station).zfill(6) + '.txt'
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temp = df.loc[df['    DATE'] == date]['   TG'].squeeze()/10

    return {
        "Station": station,
        "date": date,
        "temprature": temp
    }

if __name__ == "__main__":
    app.run(debug=True)