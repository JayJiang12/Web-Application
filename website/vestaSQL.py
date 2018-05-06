# https://www.python-course.eu/sql_python.php

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
    'param_color_blue':'color=',
    'param_color_red':'color='
}

# need to add other variables and scalable cmd 
# request is a python dict? 
def getCities(request):
    # If user did not submit any parameters, return empty list
    userInput = request.values()
    
    f = open('log.txt', 'w')
    f.write(userInput)

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
            
            # The colors need to be strings
            if (param == "param_color_blue") or (param == "param_color_red"):
                cmd = cmd + " " + PARAM_MAP[param] + "\"" + request[param] + "\""
            else:
                cmd = cmd + " " + PARAM_MAP[param] + request[param]

            moreThan2 = True

    cmd = cmd + " ORDER BY population DESC LIMIT 100;"

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
        'param_prop_min':'',
        'param_prop_max':'',
        'param_pop_min':'100000',
        'param_pop_max':'1000000',
        'param_temp_min':'40',
        'param_temp_max':'',
        'param_sun_min':'100',
        'param_sun_max':'', 
        'param_humid_min':'',
        'param_humid_max':'60', 
        'param_rain_min':'',
        'param_rain_max':'', 
        'param_snow_min':'',
        'param_snow_max':'', 
        'param_color_blue':'',
        'param_color_red':''
    }

    cities = getCities(request)
    cities = getJSON(cities)

    print(cities)
