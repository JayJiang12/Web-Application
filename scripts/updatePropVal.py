# https://www.python-course.eu/sql_python.php
# https://docs.python.org/2/library/csv.html
# api.census.gov 

import MySQLdb
import csv
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

# Read csv file 
file = open("PropertyValue.csv", 'r')
data = csv.reader(file)

# Skip header
next(data, None)

# Update cities table with political colro 
for row in data:
    city = row[1].strip()
    state = row[2].strip()
    value = int(row[6])

    cmd = (
        "UPDATE cities SET propertyValue=" + str(value) + 
        " WHERE city=\"" + city + 
        "\" AND state=\"" + state + "\";" 
    )

    cursor.execute(cmd)

connection.commit()
file.close()

# Read JSON file 
#(fill in missing cities from census data / census might be more accurate)
# Make the HTTP request.
response = urllib.request.urlopen("https://api.census.gov/data/2016/acs/acs1?get=NAME,B25075_001E&for=place:*&key=ec8369606ce877227f10a83d24e5d398a5a8ac5b"
)
assert response.code == 200

# Get returned data and encoding
data2 = response.read()
encoding = response.info().get_content_charset('utf-8')

# Use the json module to load response into a 2D list.
response_list = json.loads(data2.decode(encoding))
response_list = response_list[1:]

for row in response_list:
    if row[1] == None:
        continue

    [city, state] = row[0].split(",")

    state = state.strip()

    city = city.split(" ")
    city = city[:-1]
    city = " ".join(city)

    value = int(row[1])

    cmd = (
        "UPDATE cities SET propertyValue=" + str(value) + 
        " WHERE city=\"" + city + 
        "\" AND state=\"" + state + "\";" 
    )

    cursor.execute(cmd)

# Close database 
connection.commit()
cursor.close()
connection.close()
