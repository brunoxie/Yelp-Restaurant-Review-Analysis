import os
import pandas as pd
import ast
import json
import requests


### yelp data
# load yelp business data
# dataset can be downloaded here: https://www.dropbox.com/sh/wxdjn85kn75ecei/AACcwoaFmGtRv0B23SCUXMhsa?dl=0
path_yelp = r'Documents/GitHub/final-project-restaurant-review-research/Data'
fname_yelp_business = 'yelp_academic_dataset_business.json'

df_yelp_business = pd.read_json(os.path.join(path_yelp, fname_yelp_business), lines=True)

attributes = df_yelp_business['attributes'].apply(lambda x: {} if pd.isna(x) else x)
    
# convert the json file to regular pandas dataframe
attributes_norm = pd.json_normalize(attributes)

def norm_columns(df, column):
    column = df[column].apply(lambda x: {} if pd.isna(x) or x=='None' else x).apply(lambda x:  ast.literal_eval(x) if type(x)!=dict else x)
    column_norm = pd.json_normalize(column)
    return column_norm

attributes_norm = attributes_norm.join(norm_columns(attributes_norm, 'BusinessParking')).drop(['BusinessParking'], axis=1)
attributes_norm = attributes_norm.join(norm_columns(attributes_norm, 'Ambience')).drop(['Ambience'], axis=1)
attributes_norm = attributes_norm.join(norm_columns(attributes_norm, 'DietaryRestrictions')).drop(['DietaryRestrictions'], axis=1)

df_yelp_business = df_yelp_business.join(attributes_norm).drop(['attributes'],axis=1)

df_yelp_business.to_csv(os.path.join(path_yelp, 'df_yelp_business.csv'))

# data cleaning
df_yelp_business.rename(columns = {'postal_code':'zipcode'}, inplace=True)
df_yelp_business = df_yelp_business[df_yelp_business['zipcode']!='']
df_yelp_business = df_yelp_business[df_yelp_business["zipcode"].str.contains("T")==False]
df_yelp_business['zipcode'] = df_yelp_business['zipcode'].astype(int)
df_yelp_business = df_yelp_business[df_yelp_business["categories"].str.contains('Food|food|Restaurants')==True] #select only restaurants
df_yelp_business = df_yelp_business.replace([True,False], ['True', 'False'])
for c in ["RestaurantsAttire", "NoiseLevel", "WiFi"]:
    df_yelp_business[c] = df_yelp_business[c].str.replace("u'", "'")


### demographic data
# load demographic data
path_demo = r'Documents/GitHub/final-project-restaurant-review-research/Data'
fname_demo = 'us_county_demographics.csv'

df_demo = pd.read_csv(os.path.join(path_demo, fname_demo))

# select columns needed
df_demo = df_demo[['major_city', 
                   'county',
                   'state',
                   'zipcode',
                   'county_fips',
                   'population_estimate_2019',
                   'unemployment_unemployment_rate_2019',
                   "education_percent_of_adults_with_a_high_school_diploma_only_2015-19",
                   'population_by_gender_median_age_total_2019',
                   'population_birth_rate_2019',
                   'population_net_international_migration_rate_2019',
                   'population_net_migration_rate_2019']]

# give them less complicated names
df_demo = df_demo.rename(columns={'population_estimate_2019':'population', 
                                  'unemployment_unemployment_rate_2019':'unemployment_rate',
                                  'education_percent_of_adults_with_a_high_school_diploma_only_2015-19':'perc_education_high_school',
                                  'population_by_gender_median_age_total_2019':'median_age',
                                  'population_birth_rate_2019':'birth_rate',
                                  'population_net_international_migration_rate_2019':'international_migration_rate',
                                  'population_net_migration_rate_2019':'net_migration_rate'})

### zillow data
# use API to extract the data
def extract_zillow_data(web_option='on'):
    
    if web_option == 'on':
        
        URL = "https://files.zillowstatic.com/research/public_csvs/zhvi/Zip_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv"
        response = requests.get(URL)
        data = response.content
        with open(r"Documents/GitHub/final-project-restaurant-review-research/Data/Zillow-Data.csv", "wb") as ofile:
            ofile.write(data)
    
    path_zillow = r'Documents/GitHub/final-project-restaurant-review-research/Data'
    fname_zillow = 'Zillow-Data.csv'
    df_zillow = pd.read_csv(os.path.join(path_zillow, fname_zillow)) 
            
    return df_zillow

df_zillow = extract_zillow_data('on') 

# clean the data
df_zillow = df_zillow.melt(id_vars=df_zillow.iloc[:,:8].columns,
                           value_vars=df_zillow.iloc[:,9:-1].columns,
                           var_name='date',
                           value_name='zillow_index')
df_zillow['date'] = df_zillow['date'].astype(str)
df_zillow['month_year'] = pd.to_datetime(df_zillow.date).dt.to_period('M').dt.to_timestamp() # floor the date
df_zillow['zipcode'] = df_zillow['RegionName'].astype(int)
df_zillow = df_zillow.drop(["date", "RegionID", "RegionName", "RegionType", "StateName"], axis=1)
df_zillow = df_zillow[df_zillow['month_year']=='2019-06-01']


### merge dataset
df_merged = df_yelp_business.merge(df_demo, on='zipcode', how='left')
df_merged = df_merged.merge(df_zillow, on='zipcode', how='inner')
df_merged = df_merged.drop(['month_year', 'state_y', 'major_city', 'City', 'State'], axis=1)
df_merged = df_merged.rename(columns={'state_x':'state'})

path = r'Documents/GitHub/final-project-restaurant-review-research/Data'
df_merged.to_csv(os.path.join(path, 'df_final.csv'))
