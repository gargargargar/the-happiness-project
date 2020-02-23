#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 14:59:11 2020

@author: chrisfan
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from keras.layers import Input,Dense
from keras.models import Model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDRegressor



path = "/Users/chrisfan/Downloads/WDIData.csv"
df = pd.read_csv(path,usecols=["Country Name","Indicator Name","2017"])
df_tidy = df.pivot(values = "2017",index = "Country Name",columns = "Indicator Name")
df_tidy = df_tidy[[c for c in df_tidy if df_tidy[c].isnull().sum() < 20]]
#
path2 = "/Users/chrisfan/Downloads/world-happiness/2017.csv"
df2 = pd.read_csv(path2,usecols=["Country","Happiness Score"])
df = pd.merge(left=df_tidy, right=df2, left_on = "Country Name", right_on = "Country")

#df.to_csv("myhack2.csv")

path = "/Users/chrisfan/Desktop/myhack2.csv"
df2 = pd.read_csv(path)
df = df[df2.columns.drop(["Unnamed: 0"])]
df2 = df2.drop(["Unnamed: 0"],axis = 1)
df = df.append(df2)
df.to_csv("myhack2.csv")


df = df.dropna(axis = 0)
X_train,X_test,y_train,y_test = train_test_split(df[df.drop(["Happiness Score","Country"],axis = 1).columns],df["Happiness Score"],test_size=0.2,random_state = 42)   
#in_tensor = Input(shape=(7,))
#out_tensor = Dense(1)(in_tensor)
#model = Model(in_tensor, out_tensor)
#model.compile(optimizer = "adam",loss = "mae")
#model.fit(X_train, y_train, epochs = 2, validation_split = 0.1)
#model.evaluate(X_test,y_test)

name = X_train.columns
lasso = Lasso(alpha=0.1)
lasso.fit(X_train,y_train)
lasso_pred = lasso.predict(X_test)
score = lasso.score(X_test,y_test)

#lasso_coef = lasso.fit(X_train,y_train).coef_
#plt.plot(range(len(name)), lasso_coef)
#plt.xticks(range(len(name)), name.values, rotation=60)
#plt.margins(0.02)
#plt.show()
#mydict = {}
#for index,items in enumerate(lasso_coef):
#    mydict[items] = name[index]


#model = SGDRegressor(max_iter = 1000)
#model.fit(X_train,y_train)
#yp = model.predict(X_test)
#score = model.score(X_test,y_test)



