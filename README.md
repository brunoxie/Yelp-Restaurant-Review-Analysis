# Yelp Restaurant Review Analysis

A data analysis project using _Python_ by Bruno Xie

## Overview

This project conducts a comprehensive data analysis using Python to explore the factors affecting restaurant reviews. By leveraging both internal and external datasets, the analysis aims to provide actionable insights for restaurant entrepreneurs, enabling them to improve their business models and enhance customer satisfaction. 

## Data Source

Due to the large size of the datasets, they are stored on Dropbox. You can access the data through the following link: [Data.zip](https://www.dropbox.com/scl/fi/q1f3jlp4h8gdyfci7j1zr/Data.zip?rlkey=hwovqx121dhpabeng1ooxd3ue&st=4qm6krfv&dl=0).

The analysis uses the following datasets:

- **Internal Features:**
  - `yelp_academic_dataset_business.json`: Contains restaurant star reviews and 42 internal features.
  - `df_yelp_review.csv`: Includes customer comments for each restaurant.

- **External Features:**
  - `us_county_demographics.csv`: Demographic information at the zip code level.
  - `Zillow-Data.csv`: Average house prices by zip code, extracted via API from [Zillow](https://files.zillowstatic.com/research/public_csvs/zhvi/Zip_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv).

- **Final Datasets:**
  - `df_final.csv`: Merged dataset used for analysis.
  - `df_yelp_review.csv`: Used directly for sentiment analysis.

## Methodology

1. **Data Wrangling**
   - Raw datasets are cleaned and manipulated to create `df_final.csv` and `df_yelp_review.csv`. Merging is performed based on zip codes.

2. **Plotting**
   - **Static Plots:** Histograms, correlation plots, and boxplots are created to visualize the relationships between restaurant stars and various factors.
   - **Interactive Plots:** Shiny applications feature choropleth maps and box plots to explore demographic and restaurant feature relationships.

3. **Text Preprocessing**
   - Sentiment analysis is conducted on customer reviews to determine correlations between comments and star ratings.

4. **Statistical Analysis**
   - Regression models are fitted to assess the impacts of both microscopic and macroscopic factors on restaurant star ratings.

## Code

The project code is organized into several Python scripts:

- [`merge-data-pipeline.py`](Code/merge-data-pipeline.py): Data wrangling and merging.
- [`static-plot-visualization.py`](Code/static-plot-visualization.py): Static data visualizations.
- [`app.py`](Code/app.py): Interactive plot creation using Shiny.
- [`sentiment analysis.py`](Code/sentiment-analysis.py): Sentiment analysis and text preprocessing.
- [`regression analysis.py`](Code/regression-analysis.py): Statistical analysis and regression modeling.

## Deliverable

This project provides insights into the factors influencing restaurant reviews through visualizations and statistical analyses, which can help restaurant owners optimize their operations and marketing strategies, ultimately enhancing customer satisfaction and business success. The findings are [here](Analysis.md).
