import urllib.request
import json
import pprint
import datetime



#searches for the monthly mean temperature to be 6- between today and 2015-04-01
#datasite, start date and end date are all required, but can be altered
#to get more datasites go here: https://www.ncdc.noaa.gov/cdo-web/api/v2/datasets (must access link through below get request due to token being required)
#TEMP = searches for location that is currently 70 degrees F
#for more temperature searches go here: https://www.ncdc.noaa.gov/cdo-web/api/v2/datatypes?datacategoryid=TEMP (must access link through below get request due to token being required)

url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GSOM&datatypeid=TEMP:73&startdate=2018-03-29&enddate=2018-03-29"

url = urllib.request.Request(url)
#this adds the token to the header of the URL, this API does not all the key to be added at the end
url.add_header("token", "qxfmNuMcWnQcARsCvMDpdLNDmvNpFFug")

# Make a get request with the parameters.
response = urllib.request.urlopen(url)
assert response.code == 200

# Use the json module to load response into a list.
response_list = json.loads(response.read())

# Check the contents of the response.
pprint.pprint(response_list)
