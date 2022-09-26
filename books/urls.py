from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/1/', views.book1, name='book1'),
    path('book/2/', views.book1, name='book1'),
    path('book/3/', views.book2, name='book2'),
    path('book/4/', views.book3, name='book3'),
    path('book/5/', views.book4, name='book4'),
    path('book/6/', views.book5, name='book5'),
]