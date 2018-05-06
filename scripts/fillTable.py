# https://www.python-course.eu/sql_python.php
# https://docs.python.org/2/library/csv.html
# https://simplemaps.com/data/us-cities

import MySQLdb
import csv

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

# Read csv file 
file = open("uscitiesv1.4.csv", 'r')
data = csv.reader(file)

# Skip header
next(data, None)

# Update cities table with political colro 
for row in data:
    city = row[0]
    state = row[3]
    fips = int(row[4])
    county = row[5]
    lat = float(row[6])
    lng = float(row[7])
    
    cmd = (
        "INSERT INTO cities (city, state, county, countyFips, latitude, longitude) VALUES(\"" + 
        city + "\", \"" + 
        state + "\", \"" + 
        county + "\", " + 
        str(fips) + ", " + 
        str(lat) + ", " + 
        str(lng) + ");"
    )

    try:
        cursor.execute(cmd)
    except:
        continue

# Close database 
connection.commit()
cursor.close()
connection.close()
