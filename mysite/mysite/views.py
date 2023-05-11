from .training import initial, recommend, get_random_books, update_image_url
from django.views.decorators.csrf import csrf_exempt

# Either loads model or trains model
def init(request):
    return initial()

def coldStart(request):
    books = get_random_books()
    print(books)
    return books

@csrf_exempt
def nextThree(request):
    data = request.body.decode('utf-8')
    # bookDict = json.loads(data)
    # books = recommend(bookDict)
    # books = update_image_url(books)
    books = recommend(data)
    books = update_image_url(books)
    print(books)
    return books