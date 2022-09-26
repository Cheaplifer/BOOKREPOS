from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.template import loader
def index(request):
    latest_books_list = Book.objects.order_by('book_name')[:5]
    template = loader.get_template('index.html')
    context = {
        'book_list': latest_books_list
    }
    return HttpResponse(template.render(context, request))

def book1(request):
    return render(request, '1.html') #конечно же, это далется передачей параметра num в book и потом просто парсингом этого числа в строку, но мне лень
    #теперь это TODO))))))))))))))))))))))))))))))))))))))))

def book2(request):
    return render(request, '2.html')

def book3(request):
    return render(request, '3.html')

def book4(request):
    return render(request, '4.html')

def book5(request):
    return render(request, '5.html')
