from flask import Flask, request, json
from flask import render_template

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

from flask import Flask, request, json
from flask import render_template

class GeoLoc:
    def __init__(self, location):
        self.location = location

class UserSearch:
    #COORDINATE WITH FRONT END TEAM
    #We need to figure out how data will be sent and recieved before we progress further.
    def __init__(self, pop, propVal, temp, rainFall, snowFall, hazards, voters, radius):
        self.pop = (0, 1)   #(min, max) tuple specifying range
        self.propValue = 0
        self.temp = 73.4    #Room temp
        self.rainFall = 0   #desert
        self.snowFall = 0
        self.hazards = ["some", "hazards", "here"]
        self.voters = 50    #percentage
        self.radius = 10    #meters? who knows

    #setters and getters here if necessary (Daniel doesn't think they are necessary for the record.
class Database:
    def __init__(self, userSearch):
        self.userSearch = userSearch
        self.results = []

class CensusDB(Database):

    def buildQuery(self):
        queryString = "https://api.census.gov/data/2016/pep/population?"
        print("censusDB")
    def askDB(self):
        self.buildQuery()
        #execute API request
        results = bullshitFromAPI #data will probably need massaging


class NcdcDB(Database):

    def buildQuery(self):
        print("ncdcDB")
    def askDB(self):
        self.buildQuery()
        #execute API request
        results = bullshitFromAPI  # data will probably need massaging

class ElectionGitDB(Database):

    def buildQuery(self):
        print("electionGitDB")
    def askDB(self):
        self.buildQuery()
        #execute API request
        results = bullshitFromAPI  # data will probably need massaging

class BlsDB(Database):

    def buildQuery(self):
        self.buildQuery()
        print("blsDB")
    def askDB(self):
        #execute API request
        results = bullshitFromAPI  # data will probably need massaging

def driver():

    user = UserSearch
    #build query
        #object builds query, doesn't bother storing it
    #send query
        #object sends query, doesn't bother storing it
    #recieve results
        #query results return and stored in LIST member variable in object
    #once results are populated in member variables, can be cased with blankDB.results. Will hold List
    #store those in dictionary so that lambda function can execute on all simulataneously.

    databases = {"cDB" : CensusDB(user), "ncdcDB" : NcdcDB(user), "eGDB" : ElectionGitDB(user), "blsDB" : BlsDB(user)}
    finalResult = set()
    for key, db in databases.items():
        db.buildQuery()
        db.askDB()
        finalResult.intersection_update(key.results)
    print("Final Result: ", finalResult, "\n")
    return 0;

driver()



# <script type="text/javascript">
#     function handleSubmit() {
#       var testData = document.getElementById("testQuery").value;
#       $.ajax({
#         url: "/getPoints",
#         //make an AJAX request to the py script
#         type: "POST",
#         //pass query params below
#         data: { param: testData },
#         success: callbackFunc
#       });
#     }


# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# @app.route('/getPoints', methods=["POST"])
# def getPoints():
# 	jsdata = request.form['param']
# 	return json.dumps(jsdata);
# #    return json.dumps([[39.260261, -76.711508], [38.9307318,-77.0080818,15]])
#
# if __name__ == "__main__":
# app.run()