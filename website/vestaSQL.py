# Elizabeth Aucott
# 5/10/18
# CMSC 447 Group 4 Project
# vestaSQL.py
#
# vestaSQL.py translates a json query to an MySQL query. 
# It returns all cities in a JSON format. 
# 
# Code help from:
#     https://www.python-course.eu/sql_python.php
#     http://stackabuse.com/reading-and-writing-json-to-a-file-in-python/

import MySQLdb
import json 

PARAM_MAP = {
    'param_pop_min':'population>',
    'param_pop_max':'population<',
    'param_prop_min':'propertyValue>',
    'param_prop_max':'propertyValue<',
    'param_temp_min':'minTemp>',
    'param_temp_max':'maxTemp<', 
    'param_sun_min':'sunny>',
    'param_sun_max':'sunny<', 
    'param_humid_min':'humidity>',
    'param_humid_max':'humidity<', 
    'param_rain_min':'rain>',
    'param_rain_max':'rain<', 
    'param_snow_min':'snow>',
    'param_snow_max':'snow<', 
    'param_color':'color=',
}

# Translates a JSON query to an SQL query.
# Returns a python list of cities that match said query. 
def getCities(request):
    # If user did not submit any parameters, return empty list
    userInput = request.values()

    if all(value == "" for value in userInput):
        return([])  

    # Connect to database 
    connection = MySQLdb.connect (host = "localhost",
                                  user = "cmsc447-user",
                                  passwd = "FlyingMongeese",
                                  db = "vesta")

    cursor = connection.cursor()

    # Construct cmd to find matching cities
    moreThan2 = False
    params = [p for p in request.keys() if p.startswith("param")]

    cmd = "SELECT * FROM cities WHERE"
    
    # Add all user specified parameters 
    for param in params:
        # Only include nonempty parameters 
        if request[param] != "":
            if moreThan2:
                cmd = cmd + " AND"
            
            # The color needs to be a string
            if (param == "param_color"):
                cmd = cmd + " " + PARAM_MAP[param] + "\"" + request[param] + "\""
            # Everything else is a number 
            else:
                cmd = cmd + " " + PARAM_MAP[param] + request[param]

            moreThan2 = True

    # Add how to sort and how many results to return 
    cmd = (
        cmd + " ORDER BY " + request['order_sort_by'] + " " + 
        request['order_sort_dir'] + 
        " LIMIT " + request['limit_num'] + ";"
    )

    # Query mysql database
    print(cmd)
    cursor.execute(cmd)
    result = cursor.fetchall()

    # Close connection
    cursor.close()
    connection.close()

    return(result)

# Translates a python list into JSON list 
def getJSON(cities):
# Old list version
#    jcities = []

#    for city in cities:
#        jcities.append([city[0], [city[4], city[5]]])

#    return(json.dumps(jcities))

# New shiny JSON version 
    jcities = []

    for city in cities :
        jcities.append( {
            'name': city[0],
            'state': city[1],
            'lat': city[4],
            'lng': city[5],
            'pop': city[6],
            'prop': city[7],
            'minTemp': city[8],
            'maxTemp': city[9],
            'sunny': city[10],
            'humid': city[11],
            'rain': city[12], 
            'snow': city[13],
            'color': city[14]
        } )

    return(json.dumps(jcities))


# Test 
if __name__ == "__main__":
    request = {
        'param_prop_min':'',
        'param_prop_max':'',
        'param_pop_min':'100000',
        'param_pop_max':'1000000',
        'param_temp_min':'',
        'param_temp_max':'',
        'param_sun_min':'100',
        'param_sun_max':'', 
        'param_humid_min':'',
        'param_humid_max':'60', 
        'param_rain_min':'',
        'param_rain_max':'', 
        'param_snow_min':'',
        'param_snow_max':'', 
        'param_color':'',
        'order_sort_by':'sunny',
        'order_sort_dir':'DESC',
        'limit_num':'5'
    }

    cities = getCities(request)
    cities = getJSON(cities)

    print(cities)
