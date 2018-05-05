# https://www.python-course.eu/sql_python.php

import MySQLdb
import json 

# need to add other variables and scalable cmd 
def getCities(pop):
    # Connect to database 
    connection = MySQLdb.connect (host = "localhost",
                                  user = "cmsc447-user",
                                  passwd = "FlyingMongeese",
                                  db = "vesta")

    cursor = connection.cursor()

    # Construct cmd to find matching cities
    pop = int(pop)
    minPop = pop - 100000
    maxPop = pop + 100000

    cmd = (
        "SELECT * FROM cities WHERE " +
        "population>" + str(minPop) +
        " AND population<" + str(maxPop) + ";"
    )

    # Get database
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
    cities = getCities(1000000)
    cities = getJSON(cities)

    print(cities)
