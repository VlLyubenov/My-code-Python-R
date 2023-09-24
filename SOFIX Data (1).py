# -*- coding: utf-8 -*-

# -- Sheet --



import pandas as pd

ATERAprice = (pd.read_html("https://www.infostock.bg/infostock/control/pricestats/ATERA", match="08/2021"))



ATERAdiv = pd.read_html("https://www.infostock.bg/infostock/control/profile/ATERA", match ="За година")

ATERAincome = ["Earnings", 7323, 3435, 10777, 7841, 7611, 7081, 24726, 21455, 49199, 2438, 0, 738, 23044]

import csv

from bs4 import BeautifulSoup

import requests

url= "https://www.infostock.bg/infostock/control/ratiosGroup/DOVUHL?group=2&period=&compareWith=&ctx=ratios&periodType=1&consolidated=2"

page = requests.get(url)

soup = BeautifulSoup(page.text, "lxml")

#<table cellpadding="0" cellspacing="0" class="homeTable" width="100%">
table = soup.find("table", "homeTable")

headers=[]

for i in table.find_all("th"):
    title = i.text.strip()
    headers.append(title)



import selenium
import path

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--headless--")
options.add_argument("--no sandbox--")
options.add_argument("--disable-dev-shm-usage")

PATH = r'D:\chromedriver.exe'


wd = webdriver.Chrome("New folder/chromedriver.exe", options=options)

pd.read_html("https://www.infostock.bg/infostock/control/ratiosGroup/DOVUHL?group=2&period=&compareWith=&ctx=ratios&periodType=1&consolidated=2", match = "P/E")









# -- Sheet 2 --

import pandas as pd
import csv
from bs4 import BeautifulSoup
import requests

from pandas import DataFrame

url= "https://www.infostock.bg/infostock/control/ratiosGroup/DOVUHL?group=2&period=&compareWith=&ctx=ratios&periodType=1&consolidated=2"

page = requests.get(url)

soup = BeautifulSoup(page.text, "lxml")

table = soup.find("table", "homeTable")

data = {}

table_data = soup.find_all("tr")

rows = table.findAll('tr')
for tr in rows:
    cols = tr.findAll('td')
    for td in cols:
        print(td.find(text=True))
        

        

list = []

rows = table.findAll('tr')
for tr in rows:
    cols = find_stripped(table, "td")
   


   

def find_stripped(soup, what):
  found = soup.find(what)
  if found is not None:
    return found.text.strip()

file = open("New folder/New file.txt", "w")
rows = table.findAll('tr')
for tr in rows:
    cols = tr.findAll('td')
    for td in cols:
        print(td.find(text=True), file=file)
        


file.close()

###############################################################################################

import os
import sys
import itertools

tickers = ["BGSFA", "CCB", "CHIM", "DUH", "EUBG", "FIB","BGALB"]


urls= ["https://www.infostock.bg/infostock/control/ratiosGroup/SFARM?group=2&period=&compareWith=&ctx=ratios&periodType=1&consolidated=2",
"https://www.infostock.bg/infostock/control/ratiosGroup/CCB?group=2&period=&compareWith=&ctx=ratios&periodType=1&consolidated=2",
"https://www.infostock.bg/infostock/control/ratiosGroup/CHIM?group=2&period=&compareWith=&ctx=ratios&periodType=1&consolidated=2",
"https://www.infostock.bg/infostock/control/ratiosGroup/DOVUHL?group=2&period=&compareWith=&ctx=ratios&periodType=1&consolidated=2",
"https://www.infostock.bg/infostock/control/ratiosGroup/EUBG?group=2&period=&compareWith=&ctx=ratios&periodType=1&consolidated=2",
"https://www.infostock.bg/infostock/control/ratiosGroup/FIB?group=2&period=&compareWith=&ctx=ratios&periodType=1&consolidated=2",
        "https://www.infostock.bg/infostock/control/ratiosGroup/ALB?group=2&period=&compareWith=&ctx=ratios&periodType=1&consolidated=1"]

str = "Sofix Coef/{}.csv"

for ticker, link in zip(tickers, urls):
    path = str.format(ticker)
    file = open(path, "w")

    page = requests.get(link)
    soup = BeautifulSoup(page.text, "lxml")
    table = soup.find("table", "homeTable")
    table_data = soup.find_all("tr")
    rows = table.findAll('tr')
    for tr in rows:    
        cols = tr.findAll('td')
        for td in cols:
            print(td.find(text=True), file=file)
    


    file.close()

tickers = ["BGSFA2016", "CCB2016", "CHIM2016", "DUH2016", "EUBG2016", "FIB2016", "BGALB2016"]
urls2015= ["https://www.infostock.bg/infostock/control/ratiosGroup/SFARM?group=2&period=2016&compareWith=&ctx=ratios&periodType=1&consolidated=2",
"https://www.infostock.bg/infostock/control/ratiosGroup/CCB?group=2&period=2016&compareWith=&ctx=ratios&periodType=1&consolidated=2",
"https://www.infostock.bg/infostock/control/ratiosGroup/CHIM?group=2&period=2016&compareWith=&ctx=ratios&periodType=1&consolidated=2",
"https://www.infostock.bg/infostock/control/ratiosGroup/DOVUHL?group=2&period=2016&compareWith=&ctx=ratios&periodType=1&consolidated=2",
"https://www.infostock.bg/infostock/control/ratiosGroup/EUBG?group=2&period=2016&compareWith=&ctx=ratios&periodType=1&consolidated=2",
"https://www.infostock.bg/infostock/control/ratiosGroup/FIB?group=2&period=2016&compareWith=&ctx=ratios&periodType=1&consolidated=2",
           "https://www.infostock.bg/infostock/control/ratiosGroup/ALB?group=2&period=2016&compareWith=&ctx=ratios&periodType=1&consolidated=1"]


for ticker, link in zip(tickers, urls2015):
    path = str.format(ticker)
    file = open(path, "w")

    page = requests.get(link)
    soup = BeautifulSoup(page.text, "lxml")
    table = soup.find("table", "homeTable")
    table_data = soup.find_all("tr")
    rows = table.findAll('tr')
    for tr in rows:    
        cols = tr.findAll('td')
        for td in cols:
            print(td.find(text=True), file=file)
    


    file.close()





tickers = ["BGSFA2012", "CCB2012", "CHIM2012", "DUH2012", "EUBG2012", "FIB2012", "BGALB2012"]
urls2010= ["https://www.infostock.bg/infostock/control/ratiosGroup/SFARM?group=2&period=2012&compareWith=&ctx=ratios&periodType=1&consolidated=2",
"https://www.infostock.bg/infostock/control/ratiosGroup/CCB?group=2&period=2012&compareWith=&ctx=ratios&periodType=1&consolidated=2",
"https://www.infostock.bg/infostock/control/ratiosGroup/CHIM?group=2&period=2012&compareWith=&ctx=ratios&periodType=1&consolidated=2",
"https://www.infostock.bg/infostock/control/ratiosGroup/DOVUHL?group=2&period=2012&compareWith=&ctx=ratios&periodType=1&consolidated=2",
"https://www.infostock.bg/infostock/control/ratiosGroup/EUBG?group=2&period2012=&compareWith=&ctx=ratios&periodType=1&consolidated=2",
"https://www.infostock.bg/infostock/control/ratiosGroup/FIB?group=2&period2012=&compareWith=&ctx=ratios&periodType=1&consolidated=2",
"https://www.infostock.bg/infostock/control/ratiosGroup/ALB?group=2&period=2012&compareWith=&ctx=ratios&periodType=1&consolidated=1"]


for ticker, link in zip(tickers, urls2010):
    path = str.format(ticker)
    file = open(path, "w")

    page = requests.get(link)
    soup = BeautifulSoup(page.text, "lxml")
    table = soup.find("table", "homeTable")
    table_data = soup.find_all("tr")
    rows = table.findAll('tr')
    for tr in rows:    
        cols = tr.findAll('td')
        for td in cols:
            print(td.find(text=True), file=file)
    


    file.close()

tickers = ["BGSFA2005", "CCB2005", "CHIM2005", "DUH2005", "EUBG2005", "FIB2005"]
urls2005= ["https://www.infostock.bg/infostock/control/ratiosGroup/SFARM?group=2&period=2005&compareWith=&ctx=ratios&periodType=1&consolidated=2",
"https://www.infostock.bg/infostock/control/ratiosGroup/CCB?group=2&period=&compareWith=2005&ctx=ratios&periodType=1&consolidated=2",
"https://www.infostock.bg/infostock/control/ratiosGroup/CHIM?group=2&period=&compareWith=2005&ctx=ratios&periodType=1&consolidated=2",
"https://www.infostock.bg/infostock/control/ratiosGroup/DOVUHL?group=2&period=&compareWith=2005&ctx=ratios&periodType=1&consolidated=2",
"https://www.infostock.bg/infostock/control/ratiosGroup/EUBG?group=2&period=&compareWith=2005&ctx=ratios&periodType=1&consolidated=2",
"https://www.infostock.bg/infostock/control/ratiosGroup/FIB?group=2&period=&compareWith=2005&ctx=ratios&periodType=1&consolidated=2"]


for ticker, link in zip(tickers, urls2005):
    path = str.format(ticker)
    file = open(path, "w")

    page = requests.get(link)
    soup = BeautifulSoup(page.text, "lxml")
    table = soup.find("table", "homeTable")
    table_data = soup.find_all("tr")
    rows = table.findAll('tr')
    for tr in rows:    
        cols = tr.findAll('td')
        for td in cols:
            print(td.find(text=True), file=file)
    


    file.close()

# -- Sheet 3 --

import pandas as pd

import csv

ATERprice = pd.read_csv("sofix/ATER Historical Data.csv")

ATERprice["monthly_returns"] = ATERprice['Price'].pct_change()

ATERprice["annual_returns"] = ATERprice['Price'].pct_change(12)


List1=range(1,14)

import numpy as np

Array = (np.multiply(List1, 12)) 


ATERAnnualGrowth = ATERprice.iloc[Array]

pd.DataFrame.to_csv(ATERAnnualGrowth, "SofixAnnGrowth/ATERAnnualGrowth")

#####################################################################

tickers = ["ATER", "BGALB", "BGSFA",  "BREF", 
           "CCB", "CHIM", "DUH", "EUBG", "FIB"]

str = "sofix/{} Historical Data.csv"

for ticker in tickers:
    path = str.format(ticker)
    price = pd.read_csv(path)
    price["monthly_returns"] = price['Price'].pct_change()
    price["annual_returns"] = price['Price'].pct_change(12)
    AnnualGrowth = price.iloc[Array]
    pd.DataFrame.to_csv(AnnualGrowth, path)







# -- Sheet 4 --

import pandas as pd
import csv

Ratios = pd.read_csv("Sofix Coef/BGSFA.csv")

AnnualReturns = []
AnnualReturns = pd.read_csv("sofix/BGSFA Historical Data.csv")

PERatios = Ratios.iloc[1:5]

Dates = AnnualReturns["Date"]

PERatios["Date"] = Dates

PERatios = pd.DataFrame()

paths = ["Sofix Coef/BGSFA.csv","Sofix Coef/BGSFA2012.csv", "Sofix Coef/BGSFA2016.csv"]

for path in paths:
    
    Ratios = pd.read_csv(path).iloc[1:5]
    PERatios = PERatios.append(Ratios)
   

AnnualReturnsPE = AnnualReturns.append(PERatios)

AnnualReturnsPE["P/E"] = AnnualReturnsPE["P/E"].shift(periods=-13)

###########################################################

import os
import sys
import itertools

tickers = ["BGSFA", "CCB", "CHIM", "DUH", "EUBG", "FIB", "BGALB"]

 paths = ["Sofix Coef/{}.csv","Sofix Coef/{}2016.csv","Sofix Coef/{}2012.csv"]
 str = "Sofix Coef/{}PE"
 

for ticker in tickers:

    PERatios = pd.DataFrame()
    
    for path in paths:
        
        directory = path.format(ticker)
        PERatios = pd.read_csv(directory).iloc[1:5]
        PERatios = PERatios.append(PERatios)
        directory1 = str.format(ticker)
        PERatios.to_csv(directory1)
  

path = "Sofix Coef/{}"
str = "DataForAnalisys/{}PE"
str2 = "sofix/{} Historical Data.csv"

for ticker in tickers:
    
    directory2 = str2.format(ticker)
    AnnualReturns = []
    AnnualReturns = pd.read_csv(directory2)
    directory = path.format(ticker)
    PERatios = pd.read_csv(directory)
    AnnualReturnsPE = []
    AnnualReturnsPE = AnnualReturns.append(PERatios)
    AnnualReturnsPE["P/E"] = AnnualReturnsPE["P/E"].shift(periods=-13)
    directory1 = str.format(ticker)
    AnnualReturnsPE.to_csv(directory1)
    

paths = ["Sofix Coef/{}.csv","Sofix Coef/{}2016.csv", "Sofix Coef/{}2012.csv"]
str = "Sofix Coef/{}Div"
 

for ticker in tickers:

    DivRatios = pd.DataFrame()
    
    for path in paths:
        
        directory = path.format(ticker)
        Ratios = pd.read_csv(directory).iloc[57:61]
        DivRatios = DivRatios.append(Ratios)
        directory1 = str.format(ticker)
        DivRatios.to_csv(directory1)
    

path = "Sofix Coef/{}Div"
str = "DataForAnalisys/{}Div"
str2 = "sofix/{} Historical Data.csv"

for ticker in tickers:
    directory2 = str2.format(ticker)
    AnnualReturns = []
    AnnualReturns = pd.read_csv(directory2)
    directory = path.format(ticker)
    DivRatios = pd.DataFrame()
    DivRatios = pd.read_csv(directory)
    DivYield = pd.DataFrame()
    DivYield = AnnualReturns.append(DivRatios)
    DivYield["P/E"] = DivYield["P/E"].shift(periods=-13)
    DivYield.rename(columns={"P/E":"DividentYield"})
    directory1 = str.format(ticker)
    DivYield.to_csv(directory1)

for ticker in tickers:
    directory1 = str.format(ticker)
    sample_file = pd.read_csv(directory1)
    sample_file = sample_file.rename(columns = {"P/E":"Div"}, errors="raise")
    sample_file.to_csv(directory1)

   

 sample = pd.read_csv("Sofix Coef/BGSFA.csv")
 sample1 = pd.read_csv("DataForAnalisys/BGSFADiv")
 sample2 = pd.read_csv("DataForAnalisys/EUBGDiv")

sample1 = sample1.rename(columns = {"P/E":"Div"})

paths = ["Sofix Coef/{}.csv","Sofix Coef/{}2016.csv", "Sofix Coef/{}2012.csv"]
str = "Sofix Coef/{}FCF"
 

for ticker in tickers:

    FCFRatios = pd.DataFrame()
    
    for path in paths:
        
        directory = path.format(ticker)
        Ratios = pd.read_csv(directory).iloc[99:103]
        FCFRatios = FCFRatios.append(Ratios)
        directory1 = str.format(ticker)
        FCFRatios.to_csv(directory1)

path = "Sofix Coef/{}FCF"
str = "DataForAnalisys/{}FCF"
str2 = "sofix/{} Historical Data.csv"

for ticker in tickers:
    directory2 = str2.format(ticker)
    AnnualReturns = []
    AnnualReturns = pd.read_csv(directory2)
    directory = path.format(ticker)
    FCFRatios = pd.DataFrame()
    FCFRatios = pd.read_csv(directory)
    FCFYield = pd.DataFrame()
    FCFYield = AnnualReturns.append(FCFRatios)
    FCFYield["P/E"] = FCFYield["P/E"].shift(periods=-13)
    directory1 = str.format(ticker)
    FCFYield.to_csv(directory1)

for ticker in tickers:
    directory1 = str.format(ticker)
    sample_file = pd.read_csv(directory1)
    sample_file = sample_file.rename(columns = {"P/E":"P/FCF"}, errors="raise")
    sample_file.to_csv(directory1)



# -- Sheet 5 --

import pandas as pd

listEATER = [
0.086041593,
0.040359535,
0.126624368,
0.092127835,
0.089425449,
0.083198214,
0.290518153,
0.252085536,
0.578063682,
0.672447421,
0.028645283,
0,
]

AnnualReturnsATER = pd.read_csv("sofix/ATER Historical Data.csv")

listEATER = pd.DataFrame(listEATER)

AnnualReturnsATER = AnnualReturnsATER.append(listEATER)

AnnualReturnsATER = AnnualReturnsATER.rename(columns={0:"EPS"} , errors="raise")

AnnualReturnsATER["EPS"] = AnnualReturnsATER["EPS"].shift(-12)

AnnualReturnsATER["EPS"] = AnnualReturnsATER["EPS"].shift(-1)

AnnualReturnsATER["P/E"] =  AnnualReturnsATER["Price"] / AnnualReturnsATER["EPS"]

AnnualReturnsATER.to_csv("DataForAnalisys/ATERPE")

listATER = [
-0.021196099,
0.111784749,
-0.130736694,
0.096016919,
-0.017048525,
-0.299436024,
-0.183374457,
-0.140512278,
0.333603572,
0.285606862,
-0.070144519,
-0.241475737,
]

AnnualReturnsATER = pd.read_csv("sofix/ATER Historical Data.csv")
listATER = pd.DataFrame(listATER)
AnnualReturnsATER = AnnualReturnsATER.append(listATER)
AnnualReturnsATER = AnnualReturnsATER.rename(columns={0:"FCF"} , errors="raise")
AnnualReturnsATER["FCF"] = AnnualReturnsATER["FCF"].shift(-13)
AnnualReturnsATER["P/FCF"] =  AnnualReturnsATER["Price"] / AnnualReturnsATER["FCF"]
AnnualReturnsATER.to_csv("DataForAnalisys/ATERFCF")

listATER = [
-0.021196099,
0.111784749,
-0.130736694,
0.096016919,
-0.017048525,
-0.299436024,
-0.183374457,
-0.140512278,
0.333603572,
0.285606862,
-0.070144519,
-0.241475737,
]

AnnualReturnsATER = pd.read_csv("sofix/ATER Historical Data.csv")
listATER = pd.DataFrame(listATER)
AnnualReturnsATER = AnnualReturnsATER.append(listATER)
AnnualReturnsATER = AnnualReturnsATER.rename(columns={0:"FCF"} , errors="raise")
AnnualReturnsATER["FCF"] = AnnualReturnsATER["FCF"].shift(-13)
AnnualReturnsATER["P/FCF"] =  AnnualReturnsATER["Price"] / AnnualReturnsATER["FCF"]
AnnualReturnsATER.to_csv("DataForAnalisys/ATERFCF")

listATER = [
0.109,
0.14,
0.047,
0.106,
0.17,
0.1,
0.3,
0.3979,
0.493,
0.25,
0.048,
0.03738,
]

AnnualReturnsATER = pd.read_csv("sofix/ATER Historical Data.csv")
listATER = pd.DataFrame(listATER)
AnnualReturnsATER = AnnualReturnsATER.append(listATER)
AnnualReturnsATER = AnnualReturnsATER.rename(columns={0:"DIV"} , errors="raise")
AnnualReturnsATER["DIV"] = AnnualReturnsATER["DIV"].shift(-13)
AnnualReturnsATER["Div"] =    AnnualReturnsATER["DIV"] / AnnualReturnsATER["Price"]
AnnualReturnsATER.to_csv("DataForAnalisys/ATERDiv")

listATER = [
0.080336008,
0.145892269,
0.18526644,
0.160354483,
0.067548063,
0.057993187,
0,
0.048640379,
0.049621846,
0.325067837,
0.022949021,
0,
]

AnnualReturnsATER = pd.read_csv("sofix/BREF Historical Data.csv")
listATER = pd.DataFrame(listATER)
AnnualReturnsATER = AnnualReturnsATER.append(listATER)
AnnualReturnsATER = AnnualReturnsATER.rename(columns={0:"EPS"} , errors="raise")
AnnualReturnsATER["EPS"] = AnnualReturnsATER["EPS"].shift(-13)
AnnualReturnsATER["P/E"] =  AnnualReturnsATER["Price"] / AnnualReturnsATER["EPS"]
AnnualReturnsATER.to_csv("DataForAnalisys/BREFPE")

listATER = [
-0.544772242,
-0.245135962,
0.794844409,
-0.121932914,
0.098752959,
-0.137463195,
-0.499307199,
-0.10039836,
-0.356676866,
1.161566884,
-0.024190289,
-0.684371572,

]

AnnualReturnsATER = pd.read_csv("sofix/BREF Historical Data.csv")
listATER = pd.DataFrame(listATER)
AnnualReturnsATER = AnnualReturnsATER.append(listATER)
AnnualReturnsATER = AnnualReturnsATER.rename(columns={0:"FCF"} , errors="raise")
AnnualReturnsATER["FCF"] = AnnualReturnsATER["FCF"].shift(-13)
AnnualReturnsATER["P/FCF"] =  AnnualReturnsATER["Price"] / AnnualReturnsATER["FCF"]
AnnualReturnsATER.to_csv("DataForAnalisys/BREFFCF")

listATER = [
0.0830958,
0.1241,
0.0996096,
0.0341072,
0.0737971,
0.0797769,
0.02396,
0.06481,
0.2129171,
0.0396036,
0.039290604
]

AnnualReturnsATER = pd.read_csv("sofix/BREF Historical Data.csv")
listATER = pd.DataFrame(listATER)
AnnualReturnsATER = AnnualReturnsATER.append(listATER)
AnnualReturnsATER = AnnualReturnsATER.rename(columns={0:"DIV"} , errors="raise")
AnnualReturnsATER["DIV"] = AnnualReturnsATER["DIV"].shift(-13)
AnnualReturnsATER["Div"] =    AnnualReturnsATER["DIV"] / AnnualReturnsATER["Price"]
AnnualReturnsATER.to_csv("DataForAnalisys/BREFDiv")





# -- Sheet 6 --

import pandas as pd

tickers = ["BGSFA", "CCB", "CHIM", "DUH", "EUBG", "FIB","BGALB", "ATER", "BREF"]

SofixDataFrame = pd.DataFrame()
str = "DataForAnalisys/{}PE"

for ticker in tickers:
    path = str.format(ticker)
    DataFrame = pd.DataFrame()
    DataFrame = pd.read_csv(path)
    DataFrame.drop(range(13,25))
    SofixDataFrame["Date"] = SofixDataFrame.append(DataFrame["Date"], ignore_index=True)
    SofixDataFrame["P/E"] = SofixDataFrame.append(DataFrame["P/E"], ignore_index=True)
    SofixDataFrame["annual_returns"] = SofixDataFrame.append(DataFrame["annual_returns"], ignore_index=True)



SofixDataFrame["P/E"] = SofixDataFrame.append(DataFrame["P/E"], ignore_index=True)

str = "DataForAnalisys/{}PE"
str2 = "CSV/{}PE.csv"

for ticker in tickers:
    path = str.format(ticker)
    DataFrame = pd.DataFrame()
    DataFrame = pd.read_csv(path)
    path2 = str2.format(ticker)
    DataFrame.to_csv(path2)

str = "DataForAnalisys/{}Div"
str2 = "CSV/{}Div.csv"

for ticker in tickers:
    path = str.format(ticker)
    DataFrame = pd.DataFrame()
    DataFrame = pd.read_csv(path)
    path2 = str2.format(ticker)
    DataFrame.to_csv(path2)

###############################################

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
regr = linear_model.LinearRegression()


list = range(13,25)
ATERPE = pd.read_csv("DataForAnalisys/ATERPE")
x = np.array(ATERPE["P/E"]).reshape(1,-1)
x = x[:10]
y = np.array(ATERPE["annual_returns"])
y = y[:10]
regr.fit(x[:11], y[:11])

x = x[:10]



# -- Sheet 7 --

import pandas as pd
import numpy as np

ATERprice = pd.read_csv("ATER Historical Data Jan.csv")

ATERprice["annual_returns"] = ATERprice['Price'].pct_change(12)

List1=range(0,11)

Array = (np.multiply(List1, 12)) 

ATERAnnualGrowth = ATERprice.iloc[Array]

ATERPE = pd.read_csv("DataForAnalisys/ATERPE")

ATERPE = ATERPE.append(ATERAnnualGrowth)
ATERAnnualGrowth.to_csv("DataForAnalisys/ATERJan.csv")

tickers = ["ATER", "BGALB", "BGSFA",  "BREF", 
           "CCB", "CHIM", "DUH", "EUBG", "FIB"]

str = "DataForAnalisys/{}Div"
str2 = "DataForAnalisys/{}Div.csv"

for ticker in tickers:
    path = str.format(ticker)
    path2 = str2.format(ticker)
    data = pd.read_csv(path)
    data.to_csv(path2)

str = "DataForAnalisys/{}FCF"
str2 = "DataForAnalisys/{}FCF.csv"

for ticker in tickers:
    path = str.format(ticker)
    path2 = str2.format(ticker)
    data = pd.read_csv(path)
    data.to_csv(path2)



# -- Sheet 8 --

import pandas as pd

dosie = (pd.read_html("https://www.uni-svishtov.bg/bg/education/doctor/doctor-dosie/d010221238"))

print(dosie)

