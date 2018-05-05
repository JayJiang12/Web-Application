# https://www.python-course.eu/sql_python.php

import MySQLdb
import json 

PARAM_MAP = {
    'param_prop_min':'propertyValue>',
    'param_prop_max':'propertyValue<',
    'param_pop_min':'population>',
    'param_pop_max':'population<',
    'param_temp_min':'minTemp>',
    'param_temp_max':'maxTemp<'
}

# need to add other variables and scalable cmd 
# request is a python dict? 
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
    cmd = "SELECT * FROM cities WHERE"
    moreThan2 = False
    params = list(request.keys())

    for param in params:
        if request[param] != "":
            if moreThan2:
                cmd = cmd + " AND"

            cmd = cmd + " " + PARAM_MAP[param] + request[param]
            moreThan2 = True

    cmd = cmd + " ORDER BY population DESC;"

    # Query mysql database
    print(cmd)
    cursor.execute(cmd)
    result = cursor.fetchall()

    # Close connection
    cursor.close()
    connection.close()

    return(result)

# this needs to be changed so the JSON is more readable 
# (especially with more data)
def getJSON(cities):
    jcities = []

    for city in cities:
        jcities.append([city[0], [city[4], city[5]]])

    return(json.dumps(jcities))

if __name__ == "__main__":
    request = {
        'param_prop_min':'100000',
        'param_prop_max':'120000',
        'param_pop_min':'500000',
        'param_pop_max':'1000000',
        'param_temp_min':'',
        'param_temp_max':''
    }

    cities = getCities(request)
    cities = getJSON(cities)

    print(cities)
