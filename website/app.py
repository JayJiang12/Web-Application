from flask import Flask, request, json
from flask import render_template
import vestaSQL

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getPoints', methods=["POST"])
def getPoints():
    # Get user input
    col_slider = request.form['param_col_slider']
    temp_min = request.form['param_temp_min']
    temp_max = request.form['param_temp_max']
    pop = request.form['param_pop']

    # Get all matching cities
    cities = vestaSQL.getCities(pop)
    
    # Convert to json
    cities = vestaSQL.getJSON(cities)
    
    return(cities)

if __name__ == "__main__":
    app.run()
