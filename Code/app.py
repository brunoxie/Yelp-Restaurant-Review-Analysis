from shiny import App, render, ui
import geopandas as gpd
import os
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import numpy as np 
from scipy import stats
import seaborn as sns
# dataset can be downloaded here: https://www.dropbox.com/sh/wxdjn85kn75ecei/AACcwoaFmGtRv0B23SCUXMhsa?dl=0
path = r"/Users/apple/Desktop/Fall 2022/DPPP II/Homework/final-project-restaurant-review-research/Data"
df_final = pd.read_csv(os.path.join(path,'df_final.csv'))


### INTERACTIVE PLOT I
# Getting data that includes county fips and geometry 
# Citation: https://darribas.org/wmn/labs/lab_09_prepare_data
county_url = 'https://www2.census.gov/geo/tiger/GENZ2018/shp/cb_2018_us_county_5m.zip'
counties = gpd.read_file(county_url)
counties['county_fips'] = counties['STATEFP'] + counties['COUNTYFP']
counties['STATEFP'] = counties['STATEFP'].astype(int)
counties = counties[(counties['STATEFP']<60) & (counties['STATEFP']!=2) & (counties['STATEFP']!=15)]
counties_df = pd.DataFrame(counties)
counties_df = counties_df[['GEOID', 'county_fips', 'geometry']]
counties_df['county_fips'] = counties_df['county_fips'].astype(int)

# Creating a dataset that only contains certain demographic features
demographic = df_final[['county_fips', 'population', 'unemployment_rate', 'median_age', 'international_migration_rate', 'net_migration_rate', 'zillow_index']]

# Getting aggregated dataframe
demographic_agg = demographic.groupby('county_fips').mean().reset_index()

plot_demographic_columns = ['population',
 'unemployment_rate',
 'median_age',
 'international_migration_rate',
 'net_migration_rate',
 'zillow_index']

demographic_agg_long = pd.melt(demographic_agg, id_vars='county_fips', value_vars=plot_demographic_columns)

# Merging gemotry columns and county fips together
demographic_agg_long = demographic_agg_long.merge(counties_df, how='left', on='county_fips')
demographic_agg_long = gpd.GeoDataFrame(demographic_agg_long, crs='EPSG:4326', geometry='geometry')


### INTERACTIVE PLOT II: restaurants stars vs restaurant features
restaurant = df_final[['city','state','zipcode','stars','review_count',
                'BusinessAcceptsCreditCards',
                'RestaurantsTakeOut',
                'RestaurantsDelivery',
                'Caters',
                'WiFi',
                'OutdoorSeating',
                'HasTV',
                'RestaurantsReservations',
                'RestaurantsAttire',
                'GoodForKids',
                'RestaurantsGoodForGroups',
                'NoiseLevel']]

plot_feature_columns = ['BusinessAcceptsCreditCards',
                'RestaurantsTakeOut',
                'RestaurantsDelivery',
                'Caters',
                'WiFi',
                'OutdoorSeating',
                'HasTV',
                'RestaurantsReservations',
                'RestaurantsAttire',
                'GoodForKids',
                'RestaurantsGoodForGroups',
                'NoiseLevel']

restaurant = restaurant.replace([True,False], ['True', 'False'])
restaurant = restaurant.replace([True,False], ['True', 'False'])
restaurant = restaurant.replace('None', np.nan)
restaurant_long = pd.melt(restaurant, id_vars='stars', value_vars=plot_feature_columns)
restaurant_long = restaurant_long.dropna(subset=['value'])

    
demographic_tickers = {'population':'Population',
 'unemployment_rate':'Unemployment Rate',
 'median_age': 'Age',
 'international_migration_rate': 'International Migration Rate',
 'net_migration_rate': 'Net Mirgration Rate',
 'zillow_index': 'Rent'}

restaurant_tickers = ['BusinessAcceptsCreditCards',
                'RestaurantsTakeOut',
                'RestaurantsDelivery',
                'Caters',
                'WiFi',
                'OutdoorSeating',
                'HasTV',
                'RestaurantsReservations',
                'RestaurantsAttire',
                'GoodForKids',
                'RestaurantsGoodForGroups',
                'NoiseLevel']

# App UI 
app_ui = ui.page_fluid(
    # Adjust the styles to center everything
    ui.tags.style('#container {display: flex; flex-direction: column; align-items: center;}'),
    ui.tags.div(
        ui.h2('Demographics by US County'),
        ui.input_selectize('demographic_ticker', 'Demographics', demographic_tickers, multiple=False),
        ui.output_plot('demographic'),
        ui.h2('Restaurant Features and Their Average Rating'),
        ui.input_selectize('restaurant_ticker', 'Restaurant Features', restaurant_tickers, multiple=False),
        ui.output_plot('restaurant'),
    id="container")
)

# Server logic
def server(input, output, session):

    @output
    @render.plot
    def demographic():
        sub_demographic = demographic_agg_long[demographic_agg_long['variable'] == input.demographic_ticker()]

        fig, ax = plt.subplots(figsize=(8,8))
        counties.plot(ax=ax, color='white', edgecolor='black', linewidth=0.2)
        sub_demographic.plot(ax=ax, column='value', legend=True)
        ax.axis('off')
        return fig

    @output
    @render.plot
    def restaurant(): 
        sub_restaurant = restaurant_long[restaurant_long['variable'] == input.restaurant_ticker()]

        fig, ax = plt.subplots()
        ax2 = sns.boxplot(ax=ax, 
                    data = sub_restaurant,
                    x='value',
                    y='stars')
        
        return fig
    

# Connect everything
app = App(app_ui, server)