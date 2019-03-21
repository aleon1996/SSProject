#!/usr/bin/env python3

# Elisabetta Caldesi, Abe Leon, Leigh Campbell
# Social Sensing Project: Predicting Spotify's Next Top Hits
# Train the multiple linear regression model based on
# independent variables = number of tweets / time, retweets, sentiment, number, favorites
# dependent variable = Spotify Popularity Index

import json
import codecs
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

# load the training set from file to dictionary
data = {}
with open('trainingSet.json', 'r') as outfile:
    data = json.load(outfile)

# load the ground truths inside of dictionary
groundTruth = codecs.open('trainingSetGroundTruth.txt', encoding='utf-8', mode='r')
count = 1
for line in groundTruth:
    line = line.strip()
    line = line.split('^')
    data[str(count)]['SPI'] = int(line[1])
    count += 1

# save the data dictionary into a pandas dataframe
df_final = pd.DataFrame.from_dict(data, orient='index')
# use sklearn to perform multiple linear regression
X = df_final[['number_vs_time','rts', 'sentiment', 'number', 'favorites']]
Y = df_final[['SPI']]

regr = linear_model.LinearRegression()
regr.fit(X, Y) # weights will be stored into regr

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)

df_final.to_csv('model.csv')
