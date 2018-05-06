# mysql -u cmsc447-user -p -D vesta < cities_backup.sql

CREATE TABLE cities (
  city varchar(45) NOT NULL,
  state varchar(45) NOT NULL,
  county varchar(45) DEFAULT NULL,
  countyFips int(5) DEFAULT NULL,
  latitude double DEFAULT NULL,
  longitude double DEFAULT NULL,
  population int(11) DEFAULT NULL,
  propertyValue int(11) DEFAULT NULL,
  minTemp double DEFAULT NULL,
  maxTemp double DEFAULT NULL,
  sunny int(3) DEFAULT NULL,
  humidity int(3) DEFAULT NULL,
  rain double DEFAULT NULL,
  snow double DEFAULT NULL,
  color varchar(4) DEFAULT NULL,
  PRIMARY KEY (`city`,`state`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOAD DATA LOCAL INFILE 'cities_backup.csv'
INTO TABLE cities
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

