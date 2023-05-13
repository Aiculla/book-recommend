from ml_model_training.recommender import BookRecommender
from django.views.decorators.csrf import csrf_exempt
import json


obj = BookRecommender()
# Either loads model or trains model
def init(request):
    return obj.initial()

def coldStart(request):
    books = obj.get_random_books()
    print(books)
    return books

@csrf_exempt
def nextThree(request):
    data = request.body
    book = data.decode('utf-8')
    bookDict = json.loads(book)
    books = obj.recommend(bookDict['isbn'])
    return books


