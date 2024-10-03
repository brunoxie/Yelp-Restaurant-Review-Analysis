#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 15:08:13 2022

@author: zixuanzhao
"""

import os
import pandas as pd
import numpy as np
import statsmodels.api as sm

# dataset can be downloaded here: https://www.dropbox.com/sh/wxdjn85kn75ecei/AACcwoaFmGtRv0B23SCUXMhsa?dl=0
def regression(data_path = r'Documents/GitHub/final-project-restaurant-review-research/Data/Yelp/df_final.csv'):
    df_yelp = pd.read_csv(data_path)

    #regression analysis (internal)
    df_yelp = df_yelp.iloc[:,9:70] 
    df_yelp = df_yelp.iloc[:,0:55]
    df_yelp = df_yelp.drop(['BYOBCorkage','HairSpecializesIn','Open24Hours',
                'RestaurantsCounterService','AgesAllowed','GoodForMeal',
                'RestaurantsPriceRange2','hours','Music','BestNights','categories'], axis=1,inplace=False)

    # process Ys
    Xs = df_yelp.iloc[:,3:44]
    df_yelp['Alcohol'].unique()

    X= pd.DataFrame(np.where(Xs.isin(["u'free'","'free'","u'paid'","'paid'","u'full_bar'"
                        "'full_bar'","u'beer_and_wine'","'beer_and_wine'","True",True,
                        "u'formal'","'formal'","u'loud'","u'very_loud'","'very_loud'",
                        "'loud'"]), 1, 0),columns=Xs.columns.values)
    import statsmodels.api as sm
    X1 = X
    y1 = df_yelp['stars']
    x_add = sm.add_constant(X1)
    model = sm.OLS(y1, x_add).fit()
    print("statsmodel.api.OLS:", model.params[:])
    print(model.summary())

    #regression (external)
    df_yelp_ex = pd.read_csv(data_path)
    df_yelp_ex = df_yelp_ex.dropna(subset=['zillow_index','median_age'])

    #
    X2 = df_yelp_ex[['population','unemployment_rate','perc_education_high_school',
                    'birth_rate','international_migration_rate','net_migration_rate',
                    'zillow_index']]
    y2 = df_yelp_ex['stars']
    x_add = sm.add_constant(X2)
    model = sm.OLS(y2, x_add).fit()
    print("statsmodel.api.OLS:", model.params[:])
    print(model.summary())

data_path = r'/Users/zixuanzhao/Desktop/yelp_dataset/df_final.csv'
regression(data_path)
