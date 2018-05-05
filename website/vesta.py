import urllib.request
import json
import pprint
import datetime
import csv



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

# Okay, Here's what this does. We have 2 search cases: 1 var and 2 var. The classes must pass in the appopriate strings
# for the column headers. DictReader allows us to refer to them by that name instead of messing with irritating column
# numbers. However that means the strings need to be perfect. if it's 1 var, it'll look in that labeled column. If it is 2 var, it
# will look for a range in that labeled column. If the algo needs to be modified, The reading of the csv into the dict can
# be separated into it's own function. Or, possibly, even into the db classes themselves. Should return a list of the
# results. These should return from the class and go right into the intersecting set algo in the driver. Hit me up if you
# have questions. Cheers --5/5/2018 19:14;  Patrick T:-{D)>

def parseCSV(file, label, x, y, cityCol, stateCol):          #x = min, y = max
    queryResults = []
    with open(file, newline='') as csvfile:
        database = csv.DictReader(csvfile)
        if not y:
            for row in database:
                if row[label] == x:
                    queryResults.append(row[cityCol] + ", " + row[stateCol])
                else:
                    pass
        elif y:
            for row in database:
                if x <= row[label] and row[label] <= y:
                    queryResults.append(row[cityCol] + ", " + row[stateCol])
                else:
                    pass
    return queryResults

def driver():
    user = UserSearch
    databases = {"cDB" : CensusDB(user), "ncdcDB" : NcdcDB(user), "eGDB" : ElectionGitDB(user), "blsDB" : BlsDB(user)}
    startIntersecting = False
    finalResult = set()
    for key, db in databases.items():
        db.buildQuery()
        if not startIntersecting:
            finalResult = db.askDB()
            startIntersecting = True
        else:
            finalResult.intersection_update(db.askDB())

        #and that's it. The return to the website needs to be handled, but the logic for getting the cities that meet all requirements is done
        #FYI we need some use cases that will yiled more than one city. Because of what this does, it will likely easily
        #return a valid "no results" often. Just looking out for the end.   --5/5/2018 19:09;  Patrick T:-{D)>

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

