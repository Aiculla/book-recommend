import random
import csv
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from django.http import JsonResponse
from sklearn.neighbors import NearestNeighbors
import json


class BookRecommender:
    def __init__(self):
        self.books = None
        self.tf = None
        self.tfidf_matrix = None
        self.model_knn = None

    def get_random_books(self):
        try:
            with open('Books.csv', 'r') as f:
                reader = csv.DictReader(f)
                num_rows = sum(1 for row in reader)
                f.seek(0)
                row_indices = random.sample(range(num_rows), 3)
                books = {}
                for i, row in enumerate(reader):
                    if i in row_indices:
                        isbn = row['ISBN']
                        books[isbn] = {
                            'ISBN': row['ISBN'],
                            'Book-Title': row['Book-Title'],
                            'Book-Author': row['Book-Author'],
                            'Image-URL-L': row['Image-URL-L'],
                            'Publisher': row['Publisher'],
                            'Year-Of-Publication': row['Year-Of-Publication']
                        }
                books = [book_data for _, book_data in books.items()]
                return JsonResponse({'Success': True,'Message': books})
        except Exception as e:
            return JsonResponse({'Success': False,'Message':str(e)})

    def preprocess(self):
        self.books = pd.read_csv('Books.csv')
        self.books = self.books[['ISBN','Book-Title','Book-Author','Year-Of-Publication','Publisher','Image-URL-L']]
        self.books.dropna(inplace=True)
        return self.books

    def train_model(self):
        self.tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
        self.tfidf_matrix = self.tf.fit_transform(self.books['Book-Title'] + " " + self.books['Book-Author'] + " " + self.books['Publisher'])
        self.model_knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=4, n_jobs=-1)
        self.model_knn.fit(self.tfidf_matrix)

    def recommend(self, isbn):
        try:
            book_index = self.books[self.books['ISBN'] == isbn].index[0]
            indices = self.model_knn.kneighbors(self.tfidf_matrix[book_index], n_neighbors=7)[1]
            recommended_books_indices = indices[0][4:]
            recommended_books = self.books.iloc[recommended_books_indices].iloc[:, :4]
            return JsonResponse({'Success': True, 'Message': recommended_books.to_dict(orient='records')})
        except Exception as e:
            return JsonResponse({'Success': False, 'Message': str(e)})

    def initial(self):
        try:
            self.preprocess()
            self.train_model()
            return JsonResponse({'Success': True, 'Message': 'Successfully Trained'})
        except Exception as e:
            return JsonResponse({'Success': False, 'Message': e})

