# Restaurant Review Analysis

A data analysis project using Python by Bruno Xie

### Link to the Data

Given that the datasets used are too large to upload to GitHub, Dropbox has been utilized for data storage. Here is the [link](https://www.dropbox.com/scl/fi/q1f3jlp4h8gdyfci7j1zr/Data.zip?rlkey=hwovqx121dhpabeng1ooxd3ue&st=4qm6krfv&dl=0) to the Dropbox page.

### Research Question

The research question addressed is: What are some factors that may affect restaurant reviews? The answer to this question serves as a guidebook for restaurant entrepreneurs to develop better business models and enhance their reputations. Understanding these factors is critical in the competitive restaurant industry, where high ratings significantly influence customer choices. This analysis is conducted from two perspectives: microscopic and macroscopic.

* From a microscopic perspective, internal restaurant features are examined, such as appointment requirements, availability of Wi-Fi, and outdoor seating options. Two datasets are utilized: `yelp_academic_dataset_business.json`, which contains restaurant star reviews and 42 internal features, and `df_yelp_review.csv`, which includes customer comments for each restaurant. Identifying these internal attributes helps restaurant owners prioritize enhancements that meet customer expectations and improve their overall ratings.

* From a macroscopic perspective, external restaurant features at the zipcode/county level are investigated, including demographic information such as population, average house prices, and international migration rates. Two datasets are used: `us_county_demographics.csv`, which contains demographic information at the zip code level, and `Zillow-Data.csv`, extracted through API, which contains average house prices by zip code. Understanding the external factors allows restaurant owners to tailor their marketing strategies and outreach based on the demographics of their target areas.

### Approach

1. **Data Wrangling**

   Analysis is based on two cleaned datasets: `df_final.csv` and `df_yelp_review.csv`. All raw datasets are loaded, and data manipulation is performed. Zillow data is extracted via API from [zillowstatic.com](https://files.zillowstatic.com/research/public_csvs/zhvi/Zip_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv) and stored as `Zillow-Data.csv`. The datasets are merged into `df_final.csv` based on zip code, while `df_yelp_review.csv` is used directly for later sentiment analysis.

   > All data wrangling is completed in `merge-data-pipeline.py`.

2. **Plotting**

   Data visualization is performed to better understand the relationships between restaurant stars and other factors, aiding subsequent regression analysis. This visual exploration helps identify patterns that can inform decision-making for restaurant management.

   a) **Static Plots**

   * A histogram of restaurant stars is graphed to analyze their distribution.
   * A correlation plot is created to assess correlations among demographic factors, helping to identify potential multicollinearity in regression analysis.
   * Series of boxplots are generated to explore relationships between restaurant stars and internal features.
   * An additional analysis is conducted to examine how house prices affect the number of restaurants in each zip code area, with a fitted regression line added to illustrate causal relationships.

   > All static plots are completed in `static-plot-visualization.py`.

   b) **Interactive Plots**

   Interactive maps are created for both microscopic and macroscopic perspectives, featured on a Shiny webpage. 

   For macroscopic factors, a choropleth map displays demographics across the USA at the county level. Users can explore various demographic features, such as population and median age.

   For microscopic factors, the relationship between average ratings and restaurant features is visualized through box plots. Users can select different services in a dropdown menu on the Shiny webpage.

   > All interactive plots are completed in `app.py`.

3. **Text Preprocessing**

   Utilizing `df_yelp_review.csv`, a sentiment analysis is conducted with text processing tools to assess the correlation between customer comment text and the star ratings received by restaurants. This analysis is crucial as it provides insights into customer satisfaction, guiding owners on areas needing improvement.

   > All text preprocessing is completed in `sentiment analysis.py`.

4. **Statistical Analysis**

   Regression models are fitted based on microscopic and macroscopic factors separately to evaluate their impact on restaurant star reviews. Understanding these impacts helps restaurant owners and stakeholders optimize their operations.

   > All statistical analyses are completed in `regression analysis.py`.

### Results

1. **Regression Analysis**

   * **Microscopic Factors:** The top positively impactful attributes for star ratings include Wheelchair Accessibility (coefficient: 0.3022), Street Parking (coefficient: 0.2441), and an Intimate Atmosphere (coefficient: 0.1854). Conversely, Drive-Thru (coefficient: -0.7395), Noise Level (coefficient: -0.3192), and Touristy (coefficient: -0.2107) attributes negatively affect ratings.
   
   * **Macroscopic Factors:** A one-unit increase in international migration rate correlates with a 0.0134 unit increase in star ratings. Higher average house prices and lower unemployment rates also associate positively with star ratings.

2. **Sentiment Analysis**

   * The analysis reveals that customer sentiment aligns with restaurant star ratings. A positive correlation exists between star ratings and review polarity, indicating that higher ratings correspond to more favorable comments. This insight can help owners understand the significance of customer feedback in shaping their ratings.

### Conclusion

This analysis provides valuable insights for restaurant owners and stakeholders to enhance operational efficiency, tailor marketing strategies, and ultimately improve customer satisfaction, thus fostering a more sustainable and successful business model in the competitive restaurant landscape.
