# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 16:25:21 2020

@author: admin
"""

##importing the dataset
import pandas as pd 

data= pd.read_csv('E:\\assignment\\recomendation system\\book.csv',encoding= 'ISO-8859-1')
data.head()
data.describe()
data.info()

## so we do have 3 columns and 10000 rows and need to recomend the best book based on ratings.
## In our dataset we do have only one paraameter. i.e. rating
##So based on rating  we will recommend the mmost rated books



##ploting the rating distribuion
import seaborn as sb

sb.countplot(x='Book.Rating',data=data)
## from our visualization we can see different no of books  with counts based on their ratings


##recomendation based on ratings
rating = pd.DataFrame(data.groupby('User.ID')['Book.Rating'].count())

rating.sort_values('Book.Rating', ascending=False).head()

##we found out the top books those have got maximum ratings

##finding out the names of the respective books
most_rated_books = pd.DataFrame(['3757', '162052', '2276', '4017', '277427'], columns = ['User.ID'])

most_rated_books1=most_rated_books['User.ID'].astype(int)

most_rated_books_summary = pd.merge(most_rated_books1, data , on='User.ID')

most_rated_books_summary

##So we got the best books based on their maximum number of ratings.