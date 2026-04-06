from flask import Flask, render_template
import pandas as pd
import numpy as np
from scipy import stats
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import json
import os

app = Flask(__name__, template_folder='templates')

BASE = os.path.dirname(os.path.abspath(__file__))
df  = pd.read_csv(os.path.join(BASE, 'data', 'asian_funds_returns.csv'), parse_dates=['Date'])
df5 = pd.read_csv(os.path.join(BASE, 'data', 'asian_funds_5yr.csv'), parse_dates=['Date'])

FUNDS = ['Fidelity_Asia', 'Matthews_Asia', 'Invesco_Developing']

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)

