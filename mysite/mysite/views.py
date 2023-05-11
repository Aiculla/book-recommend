from .training import initial, recommend, get_random_books
from django.views.decorators.csrf import csrf_exempt
import json

# Either loads model or trains model
def init(request):
    return initial()

def coldStart(request):
    books = get_random_books()
    print(books)
    return books

@csrf_exempt
def nextThree(request):
    data = request.body
    book = data.decode('utf-8')
    bookDict = json.loads(book)
    print(bookDict)
    books = recommend(bookDict['isbn'])
    print(books)
    return books


