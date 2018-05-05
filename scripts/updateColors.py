# https://www.python-course.eu/sql_python.php
# https://docs.python.org/2/library/csv.html
# https://simplemaps.com/data/us-cities.import MySQLdb

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
file = open("2016_US_County_Level_Presidential_Results.csv", 'r')
data = csv.reader(file)

# Skip header
next(data, None)

# Update cities table with political colro 
for row in data:
    dem = float(row[1])
    gop = float(row[2])
    fips = row[10]

    if dem > gop:
        color = "blue"
    else:
        color = "red"

    cmd = (
        "UPDATE cities SET color='" + color + 
        "' WHERE countyFips=" + fips + ";" 
    )

    cursor.execute(cmd)

# Close database 
connection.commit()
cursor.close()
connection.close()
