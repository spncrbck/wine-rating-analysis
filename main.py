import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

wine = pd.read_csv('ref/winemag_data_v2.csv', index_col = 0)
# columns: ['country' 'description' 'designation' 'points' 'price' 'province' 'region_1' 'region_2' 'taster_name' 'taster_twitter_handle' 'title' 'variety' 'winery']

'''
pbp = wine.groupby(['province']).points.mean()
pbp.scatter(x='province', y='points')
plt.show()
'''

to_drop = ['description','region_2', 'taster_name','taster_twitter_handle']

wine.drop(to_drop, inplace=True, axis=1)

# print(wine.head(20))

country_count = wine.groupby(['country']).country.count()
country_count.plot(kind='bar', x='country', y=country_count)
plt.show()