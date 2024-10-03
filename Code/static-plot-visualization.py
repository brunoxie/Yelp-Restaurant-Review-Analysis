import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
# dataset can be downloaded here: https://www.dropbox.com/sh/wxdjn85kn75ecei/AACcwoaFmGtRv0B23SCUXMhsa?dl=0
df_final = pd.read_csv(r'Documents/GitHub/final-project-restaurant-review-research/Data/df_final.csv')

demo_list = ['population', 
             'unemployment_rate', 
             'perc_education_high_school', 
             'median_age', 
             'birth_rate', 
             'international_migration_rate', 
             'zillow_index'] # get all the demo variables for later use


### Plot 1: Distribution of restaurant star
fig, ax = plt.subplots(figsize=(8, 4))

n, bins, patches = ax.hist(df_final['stars'], bins=9, rwidth=0.8, alpha=0.8, edgecolor='grey', density=True)

ax.axvline(x = df_final['stars'].mean(), color = 'blue', linewidth=0.8, label = 'mean')

ax.legend(loc='upper right')
ax.set_xlabel("Restaurant Star")
ax.set_ylabel("Frequency")
ax.set_title("Distribution of Restaurant Star")
ax.set_xlim(bins[0],bins[-1])
plt.savefig(r"Documents/GitHub/final-project-restaurant-review-research/Images/distribution-restaurant-star.png")


### Plot 2: demographic variables correlation plot
sns.pairplot(df_final[demo_list])
plt.savefig(r"Documents/GitHub/final-project-restaurant-review-research/Images/demo-corr-plot.png")


### Plot 3: restaurant star vs demographic variables
def plot_star_demo(df, demo_list): # use a function to generate all the graphs
    
    for demo in demo_list:
        fig, ax = plt.subplots()

        sns.boxplot(x=df_final['stars'], y=df_final[demo])

        ax.set_xlabel('Restaurant Star')
        ax.set_ylabel('%s'%(demo))
        ax.set_title('Restaurant Star vs. %s'%(demo))
        plt.savefig(r"Documents/GitHub/final-project-restaurant-review-research/Images/restaurant-star-%s.png"%(demo))

plot_star_demo(df_final, demo_list)


### Plot 4: num of restaurants vs zillow house price
# want to see number of restaurants on zipcode level, need to aggregate first
df_num_resc_zillow = pd.DataFrame(df_final.groupby('zipcode')['business_id'].count())
df_num_resc_zillow = df_num_resc_zillow.rename(columns={'business_id':'num_restaurants'})
# add house price back to the new df
df_num_resc_zillow = df_num_resc_zillow.merge(df_final[['zipcode', 'zillow_index']], on='zipcode', how='left')
df_num_resc_zillow = df_num_resc_zillow[df_num_resc_zillow['zillow_index'].notna()]
df_num_resc_zillow['zillow_index'] = df_num_resc_zillow['zillow_index'].astype(int)
df_num_resc_zillow = df_num_resc_zillow[(np.abs(stats.zscore(df_num_resc_zillow['zillow_index'])) < 3)] # use z score to remove outliers

# run a simple regression to add to the graph
a, b = np.polyfit(df_num_resc_zillow['zillow_index'], df_num_resc_zillow['num_restaurants'], 1)

fig, ax = plt.subplots(figsize=(8, 4))

ax.scatter(df_num_resc_zillow['zillow_index'], df_num_resc_zillow['num_restaurants'], marker='o', alpha=0.5, s=3)
ax.plot(df_num_resc_zillow['zillow_index'], a*df_num_resc_zillow['zillow_index']+b, 
        color='grey', linewidth=1.5, linestyle='dashed',
        marker='.', markersize=0.5,
        label='fitted line')

ax.legend(loc='upper right')
ax.set_xlabel('House Price Zillow Index')
ax.set_ylabel('Number of Restaurants')
ax.set_title('House Price Zillow Index vs. Number of Restaurants')
plt.savefig(r"Documents/GitHub/final-project-restaurant-review-research/Images/num-restaurant-house-price.png")

     