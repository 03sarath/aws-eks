from flask import Flask, jsonify,request,render_template
import requests
import json

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return '''
        <html>
         <head>
        <style>
        
            /* Style the dashboard title */
      h1 {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        margin-top: 50px;
        color: #006400;
      }
            /* Add some general styling to the form */
            form {
                width: 500px;
                margin: 0 auto;
                text-align: left;
            }
            
            /* Add some spacing between form elements */
            label, input {
                margin-bottom: 10px;
                display: block;
            }
            
            /* Style the labels */
            label {
                font-weight: bold;
            }
            
            /* Style the text inputs */
            input[type='text'] {
                padding: 8px;
                width: 100%;
                box-sizing: border-box;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
            
            /* Style the submit button */
            input[type='submit'] {
                background-color: blue;
                color: white;
                padding: 12px 20px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                float: right;
            }
            
                /* Style the footer */
      footer {
        background-color: #f5f5f5;
        padding: 20px;
        text-align: center;
      }
      
      select {
    /* Add styles for the select tag here */
    padding: 10px;
    font-size: 18px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

select option {
    /* Add styles for the options here */
    padding: 10px;
    font-size: 18px;
    background-color: #eee;
}

select option:checked {
    /* Add styles for the selected option here */
    background-color: #ccc;
}

select::after {
    /* Add styles for the dropdown arrow here */
    content: "";
    background-image: url(path/to/arrow-icon.svg);
    background-repeat: no-repeat;
    width: 20px;
    height: 20px;
    position: absolute;
    right: 10px;
    top: 50%;
    transform: translateY(-50%);
}

      
        </style>
    </head>
            <body>
            <h1>Model Inference Dashboard-Psitron</h1>
            <hr>
          
         
                <form action='/predict' method='post'>
                  <h2>To get Started Enter your Server Port Number</h2>
                    <label for='Port' style='color:orange'>Port Number:</label>
                    <input type='text' value='65433' id='Port' name='Port'>
                    <br>
                 <label for='gender'>Gender:</label>
                   <select id='gender' name='gender'>
  <option value="M">M</option>
  <option value="F" selected>F</option>
</select>
                    <br>
                    <label for='ssc_p'>SSC Percentage:</label>
                    <input type='number' value='71.0' id='ssc_p' name='ssc_p'>
                    <br>
                    <label for='ssc_b'>SSC Board:</label>
                    <input type='text' value='Central' id='ssc_b' name='ssc_b'>
                    <br>
                    <label for='hsc_p'>HSC Percentage:</label>
                    <input type='number' value='58.66' id='hsc_p' name='hsc_p'>
                    <br>
                    <label for='hsc_b'>HSC Board:</label>
                    <input type='text' value='Central' id='hsc_b' name='hsc_b'>
                    <br>
                    <label for='hsc_s'>HSC Stream:</label>
                    <input type='text' value='Science' id='hsc_s' name='hsc_s'>
                    <br>
                    <label for='degree_p'>Degree Percentage:</label>
                    <input type='number' value='58.0' id='degree_p' name='degree_p'>
                    <br>
                    <label for='degree_t'>Degree Type:</label>
                    <input type='text' value='Sci&Tech' id='degree_t' name='degree_t'>
                    <br>
                    <label for='etest_p'>E-test Percentage:</label>
                    <input type='number' value='56.0' id='etest_p' name='etest_p'>
                    <br>
                    <label for='mba_p'>MBA Percentage:</label>
                    <input type='number' value='61.3' id='mba_p' name='mba_p'>
                    <br>
                     <label for='specialisation'>Any Specialisation:</label>
                    <input type='text' value='Mkt&Fin' id='specialisation' name='specialisation'>
                    <br>
                     <label for='workex'>Work Experience:</label>
                    <input type='text' value='Yes' id='workex' name='workex'>
                    <br>
                    <input type='submit' value='Predict' id='predict_button'>
                </form>
                <br>
                <br>
                <br>
                 <br>
                <footer>
      <p>Copyright &copy; 2023 Psitron Technologies Pvt.Ltd</p>
    </footer>
            </body>
        </html>
    '''

@app.route('/predict', methods=['POST', 'GET'])

def predict():
   
    candidate = [{
  "gender": request.form['gender'],
  "ssc_p":  float(request.form['ssc_p']),
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
 

    print(candidate)   
  

    port = request.form['Port']
    url = "http://recruitment-rank-app:"+ str(port) + "/predict"
    response = requests.post(url=url, json=candidate)

    if response.status_code == 200:
        output = response.json()
        #return jsonify(output)
        return render_template('result.html', result=output)
    else:
        return jsonify({'error': f'Error in evaluating features, status code: {response.status_code}'})

if __name__ == '__main__':
    app.run(debug=True)
