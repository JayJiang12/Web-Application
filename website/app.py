from flask import Flask, request, json
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getPoints', methods=["POST"])
def getPoints():
    return json.dumps({"status" : "OK"})

if __name__ == "__main__":
	app.run()
