# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 00:29:31 2020

@author: admin
"""
##recomendation based on correlations
average_rating = pd.DataFrame(data.groupby('User.ID')['Book.Rating'].mean())
average_rating['ratingCount'] = pd.DataFrame(data.groupby('User.ID')['Book.Rating'].count())
average_rating.sort_values('ratingCount', ascending=False).head()

##In this data set, the book that received the most rating counts was not highly rated at all.
## So, we need to have a better system.

##To ensure statistical significance, users with less than 150 ratings, and books with less than 100 ratings are excluded.
count = data['User.ID'].value_counts()
data = data[data['User.ID'].isin(count[count >= 150].index)]
counts = data['Book.Rating'].value_counts()
data = data[data['Book.Rating'].isin(counts[counts >= 100].index)]

##converting the ratings table to a 2D matrix
ratings_pivot = data.pivot(columns='Book.Rating')
ratings = ratings_pivot.index
userid = ratings_pivot.columns
print(ratings_pivot.shape)
ratings_pivot.head()

bones_ratings = ratings_pivot['0316666343']
similar_to_bones = ratings_pivot.corrwith(bones_ratings)
corr_bones = pd.DataFrame(similar_to_bones, columns=['pearsonR'])
corr_bones.dropna(inplace=True)
corr_summary = corr_bones.join(average_rating['ratingCount'])
corr_summary[corr_summary['ratingCount']>=300].sort_values('pearsonR', ascending=False).head(10)