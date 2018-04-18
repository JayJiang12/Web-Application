from flask import Flask, request, json
from flask import render_template
import vesta

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getPoints', methods=["POST"])
def getPoints():
    jsdata = request.form['param']
    return json.dumps(jsdata);
#    return json.dumps([[39.260261, -76.711508], [38.9307318,-77.0080818,15]])

if __name__ == "__main__":
    app.run()
