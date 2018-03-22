'''
    Elizabeth Aucott
    3/14/18
    CMSC 447 Group 4 Project
    censusquery_example.py

    Here is some sample code to query the US Census API. The sample query asks for all cities with a population between 1,000,000 and 10,000,000. 
    This code uses python3.6. All of these libraries come installed with python3. 
    Below are some very helpful links for using the API and about the dataset being queried. 

    https://www.census.gov/data/developers/guidance/api-user-guide.Overview.html
    https://www.census.gov/data/developers/data-sets/popest-popproj/popest.html
'''

import urllib.request
import json
import pprint

# Make the HTTP request.
response = urllib.request.urlopen("https://api.census.gov/data/2016/pep/population?get=GEONAME&for=place:*&DATE=9&POP=1000000:10000000&key=ec8369606ce877227f10a83d24e5d398a5a8ac5b")
assert response.code == 200

# Use the json module to load response into a list.
response_list = json.loads(response.read())

# Check the contents of the response.
pprint.pprint(response_list)
