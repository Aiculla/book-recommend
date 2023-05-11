import random
import csv
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import load_model
from sklearn.preprocessing import LabelEncoder



books = None
model = None
original_books = None


def get_random_books():
    try:
        # Open
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
            return books
    except Exception as e:
        return {"error": e}, 400


def recommend(book):
    global books, model,original_books 
    books = pd.concat([books, pd.DataFrame.from_dict([book])], axis=0, ignore_index=True) # Merge
    model = train_model() # Train the model

    # encode
    books_encoded = pd.get_dummies(books, columns=["Book-Title", "Book-Author", "Year-Of-Publication", "Publisher"])
    le = LabelEncoder()
    books_encoded["ISBN"] = le.fit_transform(books_encoded["ISBN"])
    
    book_encoded = books_encoded.iloc[-1, 1:].values 
    book_encoded = book_encoded.astype(int) 
    book_encoded_tensor = tf.convert_to_tensor(book_encoded.reshape(1, -1), dtype=tf.float32) # Convert

    # predict
    book_predicted = model.predict(book_encoded_tensor)[0]
    book_indices = book_predicted.argsort()[-3:][::-1]

    # removes input
    if book_indices[0] == books.index[-1]:
        book_indices = book_indices[1:]

    recommended_books = original_books.iloc[book_indices][["ISBN", "Book-Title", "Book-Author", "Year-Of-Publication", "Publisher", "Image-URL-L"]].to_dict(orient="records")
    return recommended_books



# Loads the model or trains if it isn't available
def initial():
    global model, books
    preprocess()
    try:
        model = load_model('book_recommender_model.h5')
        return {'Success': True}
    except:
        pass
    train_model()
    return {'Success': False}


def train_model():
    global books, model,original_books
    original_books = books.copy() # copy, forgot why?
    books = books.drop(columns=["Image-URL-L"])# drop, its not used
    books_encoded = pd.get_dummies(books, columns=["Book-Title", "Book-Author", "Year-Of-Publication", "Publisher"]) # one hot

    # label encode
    le = LabelEncoder()
    books_encoded["ISBN"] = le.fit_transform(books_encoded["ISBN"])

    # training and testing sets
    X_train = books_encoded.iloc[:-1, 1:]
    y_train = books_encoded.iloc[:-1, 0]
    X_test = books_encoded.iloc[-1:, 1:]
    y_test = books_encoded.iloc[-1:, 0]
    unique_labels = y_train.unique()

    # NN
    num_classes = len(unique_labels)
    model = Sequential([
        Dense(128, activation="relu", input_shape=(X_train.shape[1],)),
        Dense(64, activation="relu"),
        Dense(num_classes+1, activation="softmax", name="output_layer")  # Update the number of classes here
    ])
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

    # Train the model
    model.fit(X_train, y_train, epochs=1, batch_size=32, validation_data=(X_test, y_test))
    model.save('book_recommender_model.h5') # Save the model
    return model




def preprocess():
    global books
    books = pd.read_csv("Books.csv")
    books = books[["ISBN", "Book-Title", "Book-Author", "Year-Of-Publication", "Publisher", "Image-URL-L"]]
    
    # Fill missing values
    books["Book-Author"].fillna("Unknown", inplace=True)
    books["Publisher"].fillna("Unknown", inplace=True)
    books["Year-Of-Publication"].fillna(0, inplace=True)
    # Remove non-integer values from column and convert to int
    books = books[books["Year-Of-Publication"].apply(lambda x: str(x).isdigit())]
    books["Year-Of-Publication"] = books["Year-Of-Publication"].astype(int)
    books.dropna(inplace=True)
    books = books.sample(n=5000, random_state=42) #Sample
    return

# Fix issue with image
def isbn_to_image_url():
    isbn_image_url_dict = {}
    with open('Books.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            isbn_image_url_dict[row['ISBN']] = row['Image-URL-L']
    return isbn_image_url_dict
isbn_image_url_dict = isbn_to_image_url()
def update_image_url(recommended_books):
    for book in recommended_books:
        book['Image-URL-L'] = isbn_image_url_dict.get(book['ISBN'], '')
    return recommended_books
