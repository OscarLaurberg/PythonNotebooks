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
%pylab inline
import pandas as pd

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
data['INDHOLD'].astype(float).pct_change()


#Which of the 5 biggest cities has the highest percentage of 'Never Married' in 2020?


#Show a bar chart of changes in marrital status in Copenhagen from 2008 till now
#Show 2 plots in same figure: 'Married' and 'Never Married' for all ages in DK in 2020 (Hint: x axis is age from 0-125, y axis is how many people in the 2 categories). Add lengend to show names on graphs
