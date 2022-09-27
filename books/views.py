from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.template import loader
from django.shortcuts import get_object_or_404
def index(request):
    latest_books_list = Book.objects.order_by('book_name')[:5]
    template = loader.get_template('index.html')
    context = {
        'book_list': latest_books_list
    }
    return HttpResponse(template.render(context, request))

def get_book(request, book_id):
    book = get_object_or_404(Book, pk = book_id)
    return render(request, 'book.html', {'book': book})
