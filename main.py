from flask import Flask, render_template, make_response
import numpy as np
from io import BytesIO

from gen_rand import generate_normal_with_target_mean

app = Flask(__name__, template_folder='templates')

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/get_data/<mean>')
def get_data(mean):
    data = generate_normal_with_target_mean(float(mean), 30)
    buf = BytesIO()
    np.savetxt(buf, data, fmt='%.3f', delimiter=',')
    response = make_response(buf.getvalue())
    response.headers["Content-Disposition"] = "attachment; filename=data.csv"
    response.headers["Content-Type"] = "text/csv"

    return response

app.run('0.0.0.0', port=8888)