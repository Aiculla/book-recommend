import random
import csv
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from django.http import JsonResponse
from sklearn.neighbors import NearestNeighbors
import json


books = None
tf = None
tfidf_matrix = None

def get_random_books():
    try:
        with open('Books.csv', 'r') as f:
            reader = csv.DictReader(f)
            num_rows = sum(1 for row in reader)
            f.seek(0)
            # Choose three random row
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

def preprocess():
    global books
    # Load Data
    books = pd.read_csv('Books.csv')

    # Preprocessing
    books = books[['ISBN','Book-Title','Book-Author','Year-Of-Publication','Publisher','Image-URL-L']]
    books.dropna(inplace=True)


def train_model():
    global books,tf,model_knn,tfidf_matrix
    # TF-IDF Vectorizer
    tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
    tfidf_matrix = tf.fit_transform(books['Book-Title'] + " " + books['Book-Author'] + " " + books['Publisher'])

    # Nearest Neighbors Model
    model_knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=4, n_jobs=-1)
    model_knn.fit(tfidf_matrix)







# def recommend(book):
#     global books, model_knn, tf, tfidf_matrix
#     try:
#         book_df = pd.DataFrame.from_dict(book, orient='index')  
#         books = pd.concat([books, book_df.T], ignore_index=True)
#         tfidf_matrix = tf.fit_transform(books['Book-Title'] + " " + books['Book-Author'] + " " + books['Publisher'])
#         model_knn.fit(tfidf_matrix)

#         indices = model_knn.kneighbors(tfidf_matrix[-1].reshape(1, -1), n_neighbors=4)[1]
#         recommended_books_indices = indices[0][1:]
#         recommended_books = books.iloc[recommended_books_indices].iloc[:, 1:4]
#         return JsonResponse({'Success': True, 'Message': recommended_books.to_dict(orient='records')})
#     except Exception as e:
#         return JsonResponse({'Success': False, 'Message': str(e)})

# def recommend(isbn):
#     global books, tf, tfidf_matrix
#     try:
#         book_index = books[books['ISBN'] == isbn].index[0]

#         # Compute TF-IDF matrix using books DataFrame
#         tfidf_matrix = tf.fit_transform(books['Book-Title'] + " " + books['Book-Author'] + " " + books['Publisher'])

#         model_knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=4, n_jobs=-1)
#         model_knn.fit(tfidf_matrix)

#         indices = model_knn.kneighbors(tfidf_matrix[book_index].reshape(1, -1), n_neighbors=4)[1]

#         # Exclude the input book and select top 3 unique books
#         recommended_books_indices = indices[0][1:]
#         recommended_books = books.iloc[recommended_books_indices].iloc[:, 1:4]

#         return JsonResponse({'Success': True, 'Message': recommended_books.to_dict(orient='records')})
#     except Exception as e:
#         return JsonResponse({'Success': False, 'Message': str(e)})

# def recommend(isbn):
#     global books, tf, tfidf_matrix
#     try:
#         book_index = books[books['ISBN'] == isbn].index[0]

#         model_knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=4, n_jobs=-1)
#         model_knn.fit(tfidf_matrix)

#         indices = model_knn.kneighbors(tfidf_matrix[book_index], n_neighbors=10)[1]

#         # Exclude the input book and select top 3 books
#         recommended_books_indices = indices[0][1:]
#         recommended_books = books.iloc[recommended_books_indices].iloc[:, 1:4]

#         return JsonResponse({'Success': True, 'Message': recommended_books.to_dict(orient='records')})
#     except Exception as e:
#         return JsonResponse({'Success': False, 'Message': str(e)})

def recommend(isbn):
    global books, tf, tfidf_matrix
    try:
        book_index = books[books['ISBN'] == isbn].index[0]

        model_knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=4, n_jobs=-1)
        model_knn.fit(tfidf_matrix)

        indices = model_knn.kneighbors(tfidf_matrix[book_index], n_neighbors=7)[1]

        # Exclude the input book and select top 3 books. Adjust the slice to remove the first 3 recommendations.
        recommended_books_indices = indices[0][4:]
        recommended_books = books.iloc[recommended_books_indices].iloc[:, :4]

        return JsonResponse({'Success': True, 'Message': recommended_books.to_dict(orient='records')})
    except Exception as e:
        return JsonResponse({'Success': False, 'Message': str(e)})


def initial():
    try:
        preprocess()
        train_model()
        return JsonResponse({'Success': True, 'Message': 'Successfully Trained'})
    except Exception as e:
        return JsonResponse({'Success': False, 'Message': e})

# book = {
# "ISBN": "0195153448",
# "Book-Title": "Classical Mythology",
# "Book-Author": "Mark P. O. Morford",
# "Year-Of-Publication": "2002",
# "Publisher": "Oxford University Press",
# "Image-URL-L": "http://images.amazon.com/images/P/0195153448.01.LZZZZZZZ.jpg"
# }
# preprocess()
# train_model()
# recommended_books = recommend_books(book)
# print(recommended_books)




