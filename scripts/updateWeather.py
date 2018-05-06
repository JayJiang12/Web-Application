# https://www.python-course.eu/sql_python.php
# https://docs.python.org/2/library/csv.html
# https://www.currentresults.com/Weather/US/

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

# First update all state values, for any cities that might be missing
# from state csv file
# Read csv file 
file = open("StateClimate.csv", 'r')
data = csv.reader(file)

# Skip header
next(data, None)

# Update cities table with political colro 
for row in data:
    state = row[0].strip()
    minTemp = float(row[2])
    maxTemp = float(row[1])
    sunny = int(row[5])
    humidity = (int(row[6]) + int(row[7])) // 2
    rain = float(row[4])
    snow = float(row[9])

    cmd = (
        "UPDATE cities SET " +
        "minTemp=" + str(minTemp) +
        ", maxTemp=" + str(maxTemp) + 
        ", sunny=" + str(sunny) + 
        ", humidity=" + str(humidity) + 
        ", rain=" + str(rain) + 
        ", snow=" + str(snow) + 
        " WHERE state=\"" + state + "\";"
    )

    cursor.execute(cmd)

# Commit
connection.commit()
file.close()

# Then update all individual cities we have 

# Temperatures 
# Read csv file 
file = open("CityTemp.csv", 'r')
data = csv.reader(file)

# Skip header
next(data, None)

# Update cities table with political colro 
for row in data:
    state = row[0].strip()
    city = row[1].strip()
    minTemp = float(row[2])
    maxTemp = float(row[3])

    cmd = (
        "UPDATE cities SET " +
        "minTemp=" + str(minTemp) +
        ", maxTemp=" + str(maxTemp) + 
        " WHERE city=\"" + city + 
        "\" AND state=\"" + state + "\";" 
    )

    cursor.execute(cmd)

# Commit
connection.commit()
file.close()

# Precipitation 
# Read csv file 
file = open("CityRain.csv", 'r')
data = csv.reader(file)

# Skip header
next(data, None)

# Update cities table with political colro 
for row in data:
    state = row[0].strip()
    city = row[1].strip()
    rain = float(row[2])

    cmd = (
        "UPDATE cities SET " +
        "rain=" + str(rain) +
        " WHERE city=\"" + city + 
        "\" AND state=\"" + state + "\";" 
    )

    cursor.execute(cmd)

# Commit
connection.commit()
file.close()

# Snow 
# Read csv file 
file = open("CitySnow.csv", 'r')
data = csv.reader(file)

# Skip header
next(data, None)

# Update cities table with political colro 
for row in data:
    state = row[0].strip()
    city = row[1].strip()
    snow = float(row[2])

    cmd = (
        "UPDATE cities SET " +
        "snow=" + str(snow) +
        " WHERE city=\"" + city + 
        "\" AND state=\"" + state + "\";" 
    )

    cursor.execute(cmd)

# Commit
connection.commit()
file.close()

# Sun 
# Read csv file 
file = open("CitySun.csv", 'r')
data = csv.reader(file)

# Skip header
next(data, None)

# Update cities table with political colro 
for row in data:
    state = row[0].strip()
    city = row[1].strip()
    sun = int(row[2])

    cmd = (
        "UPDATE cities SET " +
        "sunny=" + str(sun) +
        " WHERE city=\"" + city + 
        "\" AND state=\"" + state + "\";" 
    )

    cursor.execute(cmd)

# Commit
connection.commit()
file.close()

# Humidity 
# Read csv file 
file = open("CityHumid.csv", 'r')
data = csv.reader(file)

# Skip header
next(data, None)

# Update cities table with political colro 
for row in data:
    state = row[0].strip()
    city = row[1].strip()
    humid = float(row[2])

    cmd = (
        "UPDATE cities SET " +
        "humidity=" + str(humid) +
        " WHERE city=\"" + city + 
        "\" AND state=\"" + state + "\";" 
    )

    cursor.execute(cmd)

# Close database 
connection.commit()
cursor.close()
connection.close()
file.close()
