import random
import csv
from django.http import JsonResponse
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity

df = None
model = None
le = None
le_title = None
le_author = None
le_publisher = None

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



# def preprocess():
#     global df, le
#     # Load the dataset
#     df = pd.read_csv('Books.csv')

#     # Fill NaNs with empty strings or mean value for the year
#     df['Book-Title'].fillna('', inplace=True)
#     df['Book-Author'].fillna('', inplace=True)
#     df['Publisher'].fillna('', inplace=True)
#     df['Year-Of-Publication'] = pd.to_numeric(df['Year-Of-Publication'], errors='coerce')
#     df['Year-Of-Publication'].fillna(df['Year-Of-Publication'].mean(), inplace=True)

#     # Encode categorical variables
#     le = LabelEncoder()
#     df['Book-Title'] = le.fit_transform(df['Book-Title'])
#     df['Book-Author'] = le.fit_transform(df['Book-Author'])
#     df['Publisher'] = le.fit_transform(df['Publisher'])

#     # Normalize year of publication
#     df['Year-Of-Publication'] = (df['Year-Of-Publication'] - df['Year-Of-Publication'].min()) / (df['Year-Of-Publication'].max() - df['Year-Of-Publication'].min())

def preprocess():
    global df, le_title, le_author, le_publisher
    # Load the dataset
    df = pd.read_csv('Books.csv')

    # Fill NaNs with empty strings or mean value for the year
    df['Book-Title'].fillna('', inplace=True)
    df['Book-Author'].fillna('', inplace=True)
    df['Publisher'].fillna('', inplace=True)
    df['Year-Of-Publication'] = pd.to_numeric(df['Year-Of-Publication'], errors='coerce')
    df['Year-Of-Publication'].fillna(df['Year-Of-Publication'].mean(), inplace=True)

    # Encode categorical variables
    le_title = LabelEncoder().fit(df['Book-Title'])
    le_author = LabelEncoder().fit(df['Book-Author'])
    le_publisher = LabelEncoder().fit(df['Publisher'])

    df['Book-Title'] = le_title.transform(df['Book-Title'])
    df['Book-Author'] = le_author.transform(df['Book-Author'])
    df['Publisher'] = le_publisher.transform(df['Publisher'])

    # Normalize year of publication
    df['Year-Of-Publication'] = (df['Year-Of-Publication'] - df['Year-Of-Publication'].min()) / (df['Year-Of-Publication'].max() - df['Year-Of-Publication'].min())

def recommend(input_book):
    # try:
        global df, le_title, le_author, le_publisher, model
        try:
        # Concatenate new book data to the dataset
            df = pd.concat([df, pd.DataFrame([input_book])], ignore_index=True)
            le_title = LabelEncoder()
            df['Book-Title'] = le_title.fit_transform(df['Book-Title'].astype(str))
            le_author = LabelEncoder()
            df['Book-Author'] = le_author.fit_transform(df['Book-Author'].astype(str))

            le_publisher = LabelEncoder()
            df['Publisher'] = le_publisher.fit_transform(df['Publisher'].astype(str))
            print('Success')
        except Exception as e:
            print(e)
        # # Encode categorical variables
        
        

        # # Retrain the autoencoder model
        # train_auto_encoder()

        # # Convert input book to suitable format
        # input_data = pd.DataFrame([input_book])
        # input_data['Book-Title'] = le_title.transform(input_data['Book-Title'].astype(str))
        # input_data['Book-Author'] = le_author.transform(input_data['Book-Author'].astype(str))
        # input_data['Publisher'] = le_publisher.transform(input_data['Publisher'].astype(str))
        # input_data['Year-Of-Publication'] = (input_data['Year-Of-Publication'] - df['Year-Of-Publication'].min()) / (
        #         df['Year-Of-Publication'].max() - df['Year-Of-Publication'].min())

        # # Convert input data to list of lists
        # input_data = [list(row) for _, row in input_data.iterrows()]

        # print('input_data shape:', len(input_data))

        # # Get the book representation from the model
        # book_representation = model.predict(input_data)

        # # Calculate similarity scores with other books
        # similarities = cosine_similarity(book_representation, model.predict(X))

        # # Get the top 3 most similar book indices
        # similar_books = similarities[0].argsort()[-4:-1][::-1]
    #     return JsonResponse({'Success': True, 'Message': df.iloc[similar_books]})
    # except Exception as e:
    #     return JsonResponse({'Success': False, 'Message': str(e)})





  # Return the corresponding book details


def train_auto_encoder():
    global model
    # Split into input (X) and output (Y)
    X = df[['Book-Title', 'Book-Author', 'Publisher', 'Year-Of-Publication']]
    Y = df['ISBN']

    # Split the data into training and testing
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

    # Define the model
    model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(X.shape[1], activation='sigmoid')
    ])

    # Compile and train the model
    model.compile(optimizer='adam', loss='mse')
    model.fit(X_train, X_train, epochs=1, validation_data=(X_test, X_test))

# def recommend(input_book):
#     try:
#         # Convert input book to suitable format
#         input_data = pd.DataFrame([input_book])
#         input_data['Book-Title'] = le.transform(input_data['Book-Title'])
#         input_data['Book-Author'] = le.transform(input_data['Book-Author'])
#         input_data['Publisher'] = le.transform(input_data['Publisher'])
#         input_data['Year-Of-Publication'] = (input_data['Year-Of-Publication'] - df['Year-Of-Publication'].min()) / (df['Year-Of-Publication'].max() - df['Year-Of-Publication'].min())

#         # add the new book to the dataset and then retrain the model

#         # Get the book representation from the model
#         book_representation = model.predict(input_data)

#         # Calculate similarity scores with other books
#         similarities = cosine_similarity(book_representation, model.predict(X))

#         # Get the top 3 most similar book indices
#         similar_books = similarities[0].argsort()[-4:-1][::-1]
#         return JsonResponse({'Success': True, 'Message': df.iloc[similar_books]})
#     except Exception as e:
#         return JsonResponse({'Success': True,'Message': str(e)})        
#   # Return the corresponding book details
   

def initial():
    try:
        preprocess()
        try:
            train_auto_encoder()
            return JsonResponse({'Success':True,'Message':'Model Successfully Loaded'})    
        except Exception as e:
            print(e,'Training')
            return JsonResponse({'Success':False,'Message':str(e)})   
    except Exception as e:
        print(e,'process')
        return JsonResponse({'Success':False,'Message':str(e)})



