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
        current_request_name = request.POST.get('aname', '')
        current_request_surname = request.POST.get('surname', '')
        if current_request_name != None and current_request_surname != None:
            try:
                au = Author.objects.get(name=current_request_name, surname=current_request_surname)
            except:
                au = None
                pass
            if au == None:
                author = Author.objects.create(name=current_request_name, surname=current_request_surname)
        bname = request.POST.get('bname', '')
        if bname != None:
            text = request.POST.get('text', '')
            author = Author.objects.get(name=current_request_name, current_request_surname=surname)
            book = Book.objects.create(name=bname, text=text, author=author)
            print(bname)
            print(book.book_name)
            print(book.id)
        return redirect('/')

def get_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book.html', {'book': book})

def delete_book(request, pk):
    book = get_object_or_404(Book, pk = pk)
    if request.method == 'POST':
        book.delete()
        return redirect('/')
    return render(request, 'index.html', {'book': book})


def delete_author(request, pk):
    authoreq = get_object_or_404(Author, pk=pk)  
    if request.method == 'POST':         
        authoreq.delete()
        book_list = Book.objects.order_by('-book_name')
        for i in book_list:
            if i.author == authoreq:
                i.delete()
        return redirect('/')

    return render(request, 'index.html', {'author': authoreq})


