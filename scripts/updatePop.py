'''
    Elizabeth Aucott
    5/3/18
    CMSC 447 Group 4 Project
    get_population.py

    get_population.py queries the US Census API for the population of all cities and saves it as a json file. The query asks for all cities (population between 0 and 10,000,000). 

    This code uses python3.6. All of these libraries come installed with python3. 
    Below are some very helpful links for using the API and about the dataset being queried. 

    https://www.census.gov/data/developers/guidance/api-user-guide.Overview.html
    https://www.census.gov/data/developers/data-sets/popest-popproj/popest.html

    Sources:
        https://stackoverflow.com/questions/32795460/loading-json-object-in-python-using-urllib-request-and-json-modules
        http://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
'''

# api.census.gov 

import MySQLdb
import urllib.request
import json 

# Connect to database 
connection = MySQLdb.connect (host = "localhost",
                              user = "cmsc447-user",
                              passwd = "FlyingMongeese",
                              db = "vesta")

connection.set_character_set('utf8')

cursor = connection.cursor()

cursor.execute('SET NAMES utf8;')
cursor.execute('SET CHARACTER SET utf8;')
cursor.execute('SET character_set_connection=utf8;')

# Make the HTTP request.
response = urllib.request.urlopen("https://api.census.gov/data/2016/pep/population?get=GEONAME&for=place:*&DATE=9&POP=0:10000000&key=ec8369606ce877227f10a83d24e5d398a5a8ac5b")
assert response.code == 200

# Get returned data and encoding
data = response.read()
encoding = response.info().get_content_charset('utf-8')

# Use the json module to load response into a 2D list.
response_list = json.loads(data.decode(encoding))
response_list = response_list[1:]

# Edit city names and insert into sql db 
for row in response_list:
    try:
        [city, state] = row[0].split(",")
    except:
        continue 

    state = state.strip()

    city = city.split(" ")
    city = city[:-1]
    city = " ".join(city)

    pop = int(row[2])

    cmd = (
        "UPDATE cities SET population=" + str(pop) + 
        " WHERE city=\"" + city + 
        "\" AND state=\"" + state + "\";" 
    )

    cursor.execute(cmd)

# Close database 
connection.commit()
cursor.close()
connection.close()

