from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    candidate = [{
        "gender": request.form['gender'],
        "ssc_p": float(request.form['ssc_p']),
        "ssc_b": request.form['ssc_b'],
        "hsc_p": float(request.form['hsc_p']),
        "hsc_b": request.form['hsc_b'],
        "hsc_s": request.form['hsc_s'],
        "degree_p": float(request.form['degree_p']),
        "degree_t": request.form['degree_t'],
        "etest_p": float(request.form['etest_p']),
        "mba_p": float(request.form['mba_p']),
        "specialisation": request.form['specialisation'],
        "workex": request.form['workex'],
    }]

    port = request.form['Port']
    url = f"http://recruitment-rank-app:{port}/predict"
    response = requests.post(url=url, json=candidate)

    if response.status_code == 200:
        output = response.json()
        return render_template('result.html', result=output)
    else:
        return jsonify({'error': f'Error in evaluating features, status code: {response.status_code}'})

if __name__ == '__main__':
    app.run(debug=True)
