import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

import pandas as pd
import numpy as np

nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')


def get_polarity(text):
    doc = nlp(text)
    return doc._.blob.polarity

# dataset can be downloaded here: https://www.dropbox.com/sh/wxdjn85kn75ecei/AACcwoaFmGtRv0B23SCUXMhsa?dl=0
review_path = "/Users/zixuanzhao/Desktop/yelp_dataset/df_yelp_review.csv"
df_review = pd.read_csv(review_path, encoding='utf-8')
df_review = df_review[['text', 'stars_x']]
df_review = df_review.groupby('stars_x')

output = []
stars = []
for star, group in df_review:
    print(f"Star: {star}")
    sents = []
    for text in group['text']:
        polarity = get_polarity(text)
        sents.append(polarity)

    mean_polarity = np.mean(sents)
    output.append(mean_polarity)
    stars.append(star)
    print(f"Mean polarity: {mean_polarity}")
    print(
        f"For star {star}, the mean polarity is {'Positive' if mean_polarity > 0 else 'Negative' if mean_polarity < 0 else 'Neutral'}")
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(stars, output, '-o')
plt.xticks(rotation=90)
plt.ylabel("Sentiment")
plt.xlabel("Stars")
plt.title('Sentiment Over Stars Rating(Using Mean Polarity)')
plt.savefig('/Users/zixuanzhao/Documents/GitHub/final-project-restaurant-review-research/Images/Sentiment_Over_Stars.png')
plt.show()