import pandas as pd


#Will accept the range of property values inputted by the user and will return the state and City
#names in which the most recent property values are within those ranges

def propertyValue(minValue, maxValue):
  data = pd.read_csv('http://files.zillowstatic.com/research/public/City/City_Zhvi_AllHomes.csv')


  stateCity = []
  minValue = int(minValue) #userinput
  maxValue = int(maxValue) #userinput
  j = 0 

  mostRecentValue = data.iloc[ :, -1:] #copy the last column over
  stateCity = data.iloc[ :, 2:4] #copy the state name and City


  cityList = ((mostRecentValue <= maxValue) & (mostRecentValue > minValue)).all(axis=1) #test to see if most recent value is within range and will return either True or False


  #go through the list of boolean values and remove the state and city if there most recent property value is not within range
  for x in cityList:
    if(cityList[j] == False):
      stateCity.drop(stateCity.index[j]) #remove the state and city from list
    j += 1

  return stateCity #return 2 column list with the State and City name




