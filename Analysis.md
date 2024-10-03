# Yelp Restaurant Review Analysis

## Introduction

In the competitive restaurant industry, high ratings significantly influence customer choices. This report explores various factors affecting restaurant reviews from both microscopic (internal features) and macroscopic (external demographic factors) perspectives. The goal is to provide restaurant owners and stakeholders with actionable insights to improve their business models and enhance their reputations.

## Research Question

The central question guiding this analysis is: **What are some factors that may affect restaurant reviews?** This inquiry is critical for understanding how restaurant attributes and external demographics influence customer perceptions and ratings.

## Microscopic Analysis

### Internal Restaurant Features

The internal features examined in this analysis include:

- Appointment requirements
- Availability of Wi-Fi
- Outdoor seating options

Using the `yelp_academic_dataset_business.json`, which contains restaurant star reviews and 42 internal features, along with `df_yelp_review.csv` for customer comments, we identify key attributes that help restaurant owners enhance their services based on customer expectations.

### Key Findings

Regression analysis reveals that the top positively impactful attributes for star ratings include:

- **Wheelchair Accessibility** (coefficient: 0.3022)
- **Street Parking** (coefficient: 0.2441)
- **Intimate Atmosphere** (coefficient: 0.1854)

Conversely, attributes that negatively affect ratings include:

- **Drive-Thru** (coefficient: -0.7395)
- **Noise Level** (coefficient: -0.3192)
- **Touristy** (coefficient: -0.2107)

## Macroscopic Analysis

### External Restaurant Features

External features at the zipcode/county level, such as demographic information, were analyzed. The datasets utilized include `us_county_demographics.csv` and `Zillow-Data.csv`.

### Key Findings

A one-unit increase in international migration rate correlates with a **0.0134 unit increase in star ratings**. Additionally, higher average house prices and lower unemployment rates are associated positively with star ratings.

## Sentiment Analysis

By utilizing `df_yelp_review.csv`, sentiment analysis shows a positive correlation between customer sentiment and restaurant star ratings. Higher ratings correspond to more favorable comments, indicating the importance of customer feedback in shaping restaurant perceptions.

## Conclusion

This analysis provides restaurant owners with valuable insights into factors influencing customer satisfaction and ratings. By focusing on identified internal features and understanding external demographic impacts, restaurant entrepreneurs can enhance operational efficiency, tailor marketing strategies, and ultimately foster a more sustainable and successful business model in the competitive restaurant landscape.
