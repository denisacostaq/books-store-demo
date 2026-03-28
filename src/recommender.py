import pandas as pd
import numpy as np

def execute():
    # Load books dataset
    books = pd.read_csv('resources/dataset/books/BX-Books.csv', sep=';', encoding='latin-1', on_bad_lines='warn')
    print(books.shape)
    print(books.columns)
    print(books.info())
    print(books.head())
    print(books.iloc[237]['Image-URL-L'])
    books = books[['ISBN', 'Book-Title', 'Book-Author', 'Year-Of-Publication', 'Publisher', 'Image-URL-L']]
    books.rename(columns={'Book-Title': 'title', 'Book-Author': 'author', 'Year-Of-Publication': 'year', 'Publisher': 'publisher', 'Image-URL-L': 'image_url'}, inplace=True)
    print(books.head())

    # Load users dataset
    users = pd.read_csv('resources/dataset/books/BX-Users.csv', sep=';', encoding='latin-1', on_bad_lines='warn')
    print(users.shape)
    print(users.columns)
    print(users.info())
    print(users.head())
    users.rename(columns={"User-ID": "user_id", "Location": "location", "Age": "age"}, inplace=True)
    print(users.head())

    # Load ratings dataset
    ratings = pd.read_csv('resources/dataset/books/BX-Book-Ratings.csv', sep=';', encoding='latin-1', on_bad_lines='warn')
    print(ratings.shape)
    print(ratings.columns)
    print(ratings.info())
    print(ratings.head())
    ratings.rename(columns={"User-ID": "user_id", "Book-Rating": "rating"}, inplace=True)
    print(ratings.head())

    print(books.shape, users.shape, ratings.shape, sep='\n')

    # Number if votes per user
    print(ratings['user_id'].value_counts())

    # Let's store only users with more than 200 ratings
    active_users = ratings['user_id'].value_counts() > 200
    print(active_users)
    indexes = active_users[active_users].index
    # find all ratings for those active users
    ratings = ratings[ratings['user_id'].isin(indexes)]
    # merge books with ratings
    books_with_rating = ratings.merge(books, on='ISBN')
    print(books_with_rating.shape)
    print(books_with_rating.head())

    number_ratings_per_book = books_with_rating.groupby('title')['rating'].count().reset_index()
    number_ratings_per_book.rename(columns={'rating': 'number_ratings'}, inplace=True)
    print(number_ratings_per_book.head())

    final_ratings = books_with_rating.merge(number_ratings_per_book, on='title')
    # filter books with at least 50 ratings
    final_ratings = final_ratings[final_ratings['number_ratings'] >= 50]
    print(final_ratings.shape)
    print(final_ratings.head())

    # let's drop duplicates
    final_ratings.drop_duplicates(subset=['user_id', 'title'], inplace=True)
    print(final_ratings.shape)
    print(final_ratings.head())