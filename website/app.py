from flask import Flask, request, json
app = Flask(__name__)

@app.route("/getPoints", methods=["POST"])
def getPoints():

    return json.dumps({"status" : "OK"})

if __name__ == "__main__":
	app.run()
