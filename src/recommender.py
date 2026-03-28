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