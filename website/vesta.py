import urllib.request
import json
import pprint
import datetime


class GeoLoc:
    def __init__(self, location):
        self.location = location

class UserSearch():
    #COORDINATE WITH FRONT END TEAM
    #We need to figure out how data will be sent and recieved before we progress further.
    def __init__(self, tempMin, tempMax, pop):
        self.tempMin = tempMin  # Room temp
        self.tempMax = tempMax  # Room temp
        self.pop = pop  # (min, max) tuple specifying range
        # self.costOfLiving = 100
        # self.propValue = 0
        # self.temp = 73.4    #Room temp
        # self.rainFall = 0   #desert
        # self.snowFall = 0
        # self.hazards = ["some", "hazards", "here"]
        # self.voters = 50    #percentage
        # self.radius = 10    #meters? who knows


    #setters and getters here if necessary (Daniel doesn't think they are necessary for the record.
class Database:
    def __init__(self, userSearch):
        self.userSearch = userSearch
        self.results = []


class CensusDB(Database):
    def __init__(self, userSearch):
        super().__init__(userSearch)
    def buildQuery(self, userSearch):
        popCenter = (int(userSearch.pop))
        popMin = popCenter - (popCenter * .20)
        popMax = popCenter + (popCenter * .20)
        url = "https://api.census.gov/data/2016/pep/population?get=GEONAME&for=place:*&DATE=9&POP=" + str(int(popMin)) + ":" + str(int(popMax)) + "&key=ec8369606ce877227f10a83d24e5d398a5a8ac5b"
        
        response = urllib.request.urlopen(url)
        #assert response.code == 200
        # Use the json module to load response into a list.
        response_list = json.loads(response.read())
        # Check the contents of the response.
        return response_list

    def askDB(self, userSearch):
        return self.buildQuery(userSearch)
        #execute API request


class NcdcDB(Database):
    def __init__(self, userSearch):
        super().__init__(userSearch)
    def buildQuery(self, userSearch):
        now = datetime.datetime.now()
        start = now.date() + datetime.timedelta(-30)
        temp = (int(userSearch.tempMin) + int(userSearch.tempMax))/2
        url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GSOM&datatypeid=TEMP:" + str(int(temp)) + "&startdate=" + str(start) + "&enddate=" + str(now)
        
        url = urllib.request.Request(url)
        # this adds the token to the header of the URL, this API does not all the key to be added at the end
        url.add_header("token", "qxfmNuMcWnQcARsCvMDpdLNDmvNpFFug")

        # Make a get request with the parameters.
        response = urllib.request.urlopen(url)
        assert response.code == 200

        # Use the json module to load response into a list.
        response_list = json.loads(response.read())

        # Check the contents of the response.
        return response_list

    def askDB(self, userSearch):
        return self.buildQuery(userSearch)
        #execute API request
        # results = bullshitFromAPI  # data will probably need massaging


class ElectionGitDB(Database):
    def buildQuery(self):
        print("electionGitDB")
    def askDB(self):
        self.buildQuery()
        #execute API request
        # results = bullshitFromAPI  # data will probably need massaging


class BlsDB(Database):
    def buildQuery(self):
        self.buildQuery()
        print("blsDB")
    def askDB(self):
        pass
        #execute API request
        # results = bullshitFromAPI  # data will probably need massaging


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
#TODO final result needs to be initialized with some data because the intersection between nothing and something is nothing
    finalResult = set()
    for key, db in databases.items():
        db.buildQuery()
        db.askDB()
        finalResult.intersection_update(db.results)
    print("Final Result: ", finalResult, "\n")
    return 0;


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

