#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 13:22:54 2020

@author: chrisfan
"""

import pandas as pd 
path = "/Users/chrisfan/Downloads/WDIData.csv"
df = pd.read_csv(path,usecols=["Country Name","Indicator Name","2015"])
df_tidy = df.pivot(values = "2015",index = "Country Name",columns = "Indicator Name")
df_tidy = df_tidy[[c for c in df_tidy if df_tidy[c].isnull().sum() < 20]]
path2 = "/Users/chrisfan/Downloads/world-happiness/2015.csv"
df2 = pd.read_csv(path2,usecols=["Country","Happiness Score"])
df2015 = pd.merge(left=df_tidy, right=df2, left_on = "Country Name", right_on = "Country")
path = "/Users/chrisfan/Downloads/WDIData.csv"
df = pd.read_csv(path,usecols=["Country Name","Indicator Name","2016"])
df_tidy = df.pivot(values = "2016",index = "Country Name",columns = "Indicator Name")
df_tidy = df_tidy[[c for c in df_tidy if df_tidy[c].isnull().sum() < 20]]
path2 = "/Users/chrisfan/Downloads/world-happiness/2016.csv"
df2 = pd.read_csv(path2,usecols=["Country","Happiness Score"])
df2016 = pd.merge(left=df_tidy, right=df2, left_on = "Country Name", right_on = "Country")
path = "/Users/chrisfan/Downloads/WDIData.csv"
df = pd.read_csv(path,usecols=["Country Name","Indicator Name","2017"])
df_tidy = df.pivot(values = "2017",index = "Country Name",columns = "Indicator Name")
df_tidy = df_tidy[[c for c in df_tidy if df_tidy[c].isnull().sum() < 20]]
path2 = "/Users/chrisfan/Downloads/world-happiness/2017.csv"
df2 = pd.read_csv(path2,usecols=["Country","Happiness Score"])
df2017 = pd.merge(left=df_tidy, right=df2, left_on = "Country Name", right_on = "Country")
dfnew = df2016.append(df2015)
dfnew = dfnew.append(df2017)

from sklearn.model_selection import train_test_split
dfnew.fillna(dfnew.mean(), inplace=True)
X_train,X_test,y_train,y_test = train_test_split(dfnew[dfnew.drop(["Happiness Score","Country"],axis = 1).columns],dfnew["Happiness Score"],test_size=0.2,random_state = 42)

from sklearn.linear_model import Lasso
lasso = Lasso(alpha=0.1)
lasso.fit(X_train,y_train)
lasso_pred = lasso.predict(X_test)
score = lasso.score(X_test,y_test)