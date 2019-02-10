import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# Creation of data visualizations for project explanation
# Ester Zhao, 2/09/2019

# -------Infant mortality rate based on race 2009 ------------
from data import race_to_infant_mortality_rate

#Create variables:
white = race_to_infant_mortality_rate.get("White")
white2009 = white[18]
black = race_to_infant_mortality_rate.get("Black")
black2009 = black[18]
hispanic = race_to_infant_mortality_rate.get("Hispanic")
hispanic2009 = hispanic[18]
asian = race_to_infant_mortality_rate.get("Asian")
asian2009 = asian[18]

#Create the Infant mortality based on race bar graph
raceCategories = ('White', 'Black', 'Hispanic', 'Asian')
y_pos = np.arange(len(raceCategories))
races = [white2009, black2009, hispanic2009, asian2009]

plt.bar(y_pos, races, align='center', alpha=0.5)
plt.xticks(y_pos, raceCategories)
plt.xlabel('Race')
plt.ylabel('Infant Mortality Percentage (%)')
plt.title('Infant Mortality Rates in MA based on Race: 2009')
plt.show()

# ------- Location based racial demographics ------------
from data import city_to_races

#Example using Boston
bostonDemographics = city_to_races.get("Boston")
bostonWhite = bostonDemographics[0]
bostonBlack = bostonDemographics[1]
bostonHispanic = bostonDemographics[2]
bostonAsian = bostonDemographics[3]

#Create the city demographics chart
y_pos = np.arange(len(raceCategories))
percentages = [bostonWhite, bostonBlack, bostonHispanic, bostonAsian]

plt.bar(y_pos, percentages, align='center', alpha=0.5)
plt.xticks(y_pos, raceCategories)
plt.xlabel('Race')
plt.ylabel('Percentage of City Residents (%)')
plt.title('Racial Demographics in Boston, MA: 2009')
plt.show()

# ------- Example comparison of hospital data ------------
from data import city_to_hospital_dict

bostonHospitals = city_to_hospital_dict.get("Boston")
numHospitals = len(bostonHospitals)

# New array values
hospitalNames = []
hospitalRates= []

for i in range(numHospitals):
    hospital = bostonHospitals[i]
    hospitalNames.append(hospital[0])
    hospitalRates.append(hospital[1])

#Create graph for city hospital pre-natal care rates
y_pos = np.arange(len(hospitalNames))

plt.bar(y_pos, hospitalRates, align='center', alpha=0.5)
plt.xticks(y_pos, hospitalNames, rotation = "vertical")
plt.xlabel('Hospital')
plt.ylabel('Pre-natal Care Rating')
plt.title('Hospital Pre-Natal Care Ratings in Boston, MA: 2009')
plt.show()
