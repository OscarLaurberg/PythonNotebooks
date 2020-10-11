#Ex1 Use data from Danmarks Statistik - Databanken
#Go to https://www.dst.dk/da/Statistik/brug-statistikken/muligheder-i-statistikbanken/api#testkonsol
#Open 'Konsol' and click 'Start Konsol'
#In the console at pt 1: choose 'Retrieve tables', pt 2: choose get request and json format and pt 3: execute:
#check the result
#in the code below this same get request is used to get information about all available data tables in 'databanken'.
#Change pt. 1 in the console to 'Retrieve data', pt 2: 'get request' and Table id: 'FOLK1A', format: csv, delimiter: semicolon and click: 'Variable and value codes' and choose some sub categories (Hint: hover over the codes to see their meaning). Finally execute and see what data you get.
#With data aggregation and data visualization answer the following questions:
#What is the change in pct of divorced danes from 2008 to 2020?
#Which of the 5 biggest cities has the highest percentage of 'Never Married' in 2020?
#Show a bar chart of changes in marrital status in Copenhagen from 2008 till now
#Show 2 plots in same figure: 'Married' and 'Never Married' for all ages in DK in 2020 (Hint: x axis is age from 0-125, y axis is how many people in the 2 categories). Add lengend to show names on graphs

import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def downloadFile(url):
  response = requests.get(url)
  fname = response.headers['Content-Disposition'].split('=')[1]
  fname = 'data/' + fname
  if response.ok:
    with open (fname, 'wb') as file_object:
      file_object.write(response.content)
    return fname

url = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&Tid=2008K1%2C2020K3&CIVILSTAND=F'

data = pd.read_csv(downloadFile(url), sep = ';')
print(data['INDHOLD'].astype(float).pct_change())


#Which of the 5 biggest cities has the highest percentage of 'Never Married' in 2020?

url = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&OMR%C3%85DE=*&K%C3%98N=TOT&ALDER=IALT&CIVILSTAND=U%2CTOT&Tid=2020K3'
df = pd.read_csv(downloadFile(url), sep = ';')
top5_cities = ['København','Aarhus','Odense','Aalborg', 'Esbjerg']
percentages = {}

for city in top5_cities:
    totalCitizens = df.loc[(df['OMRÅDE'] == city) & (df['CIVILSTAND'] == 'I alt')].iloc[0][5]
    print(totalCitizens);
    unMarried = df.loc[(df['OMRÅDE'] == city) & (df['CIVILSTAND'] == 'Ugift')].iloc[0][5]
    percentage = (unMarried / totalCitizens) * 100
    percentages[city] = percentage;

print(percentages);
highestPercentage = max(percentages.values())
city = max(percentages, key=percentages.get)

print('{} is the city with highest percentage of never married citizens, with {:.2f} %'.format(city,highestPercentage))

#Show a bar chart of changes in marrital status in Copenhagen from 2008 till now

url = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&OMR%C3%85DE=101&CIVILSTAND=G&Tid=2008K1%2C2009K1%2C2010K1%2C2011K1%2C2012K1%2C2013K1%2C2014K1%2C2015K1%2C2016K1%2C2017K1%2C2018K1%2C2019K1%2C2020K1'

df = pd.read_csv(downloadFile(url), sep=';')
start = '2008K1';
#rows = df.loc[df['TID'] == start];
marriedOrSep2008Q1 = df.loc[(df['TID'] == start)].iloc[0][3]
print(marriedOrSep2008Q1)
values = tuple(list(df['INDHOLD']))
time = tuple(list(df['TID']))
valuesSubtracted = []

for value in values:
  value -= marriedOrSep2008Q1
  valuesSubtracted.append(value);


df_plot = pd.DataFrame({'Time':time,'Changes':valuesSubtracted})
ax = df_plot.plot.bar(x='Time', y='Changes');


#Show 2 plots in same figure: 'Married' and 'Never Married' for all ages in DK in 2020 (Hint: x axis is age from 0-125, y axis is how many people in the 2 categories). Add lengend to show names on graphs

url ='https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&CIVILSTAND=G%2CU&ALDER=*'
df = pd.read_csv(downloadFile(url), sep=';')
ages = df.ALDER.unique()
ages = np.delete(ages,0)
ageSpan = len(ages)
married = df.loc[(df['CIVILSTAND'] == 'Gift/separeret'), 'INDHOLD'].tolist()
married.pop(0)
notMarried = df.loc[(df['CIVILSTAND'] == 'Ugift'), 'INDHOLD'].tolist()
notMarried.pop(0)
print(notMarried)
print(married)



# DIDNT GET THe PLOT TO WORK - BUT I GOT THE CORRECT DATA IN LISTS ABOVE

# DIDNT GET THe PLOT TO WORK - BUT I GOT THE CORRECT DATA IN LISTS ABOVE
data = [notMarried,married]


X = np.arange(3)
plt.bar(X + 0.00, data[1], color = 'b', width = 0.25,)
plt.bar(X + 0.25, notMarried[0], color = 'g', width = 0.25, label='not married')

# Add xticks on the middle of the group bars
plt.xlabel('age', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(married))], ['A', 'B', 'C', 'D', 'E'])
 
# Create legend & Show graphic
plt.legend()
plt.show()

plt.bar(0.15, married, width = 0.3)
plt.bar(0.15, notMarried, width = 0.3)
#setting the xticks. Note x1 and x2 are tuples, thus + is concatenation
plt.xticks(range(0, 125)) 
plt.show()