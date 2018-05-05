from flask import Flask, request, json
from flask import render_template
import vestaSQL

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getPoints', methods=["POST"])
def getPoints():
    # Get all matching cities
    cities = vestaSQL.getCities(request.form)
    
    # Convert to json
    cities = vestaSQL.getJSON(cities)
    
    return(cities)

if __name__ == "__main__":
    app.run()
