from contextlib import redirect_stderr
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from .models import Book, Author

def index(request):
    if request.method == 'GET':
        book_list = Book.objects.order_by('-book_name')
        template = loader.get_template('index.html')
        context = {
            'book_list': book_list
        }
        return HttpResponse(template.render(context, request))
    if request.method == 'POST':
        aname = request.POST.get('aname', '')
        surname = request.POST.get('surname', '')
        if aname != None and surname != None:
            try:
                au = Author.objects.get(name=aname, surname=surname)
            except:
                au = None
                pass
            if au == None:
                author = Author.objects.create(name=aname, surname=surname)
        bname = request.POST.get('bname', '')
        if bname != None:
            text = request.POST.get('text', '')
            author = Author.objects.get(name=aname, surname=surname)
            book = Book.objects.create(name=bname, text=text, author=author)
            print(bname)
            print(book.name)
            print(book.id)
        return redirect('/')

def get_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book.html', {'book': book})
