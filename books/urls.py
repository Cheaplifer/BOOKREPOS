from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/', views.get_book, name='view_book'),
    re_path(r'^delete/(?P<pk>[0-9]+)/$', views.delete_book, name='delete_book'),
    re_path(r'^delete/author/(?P<pk>[0-9]+)/$', views.delete_author, name='delete_author') #я это скопипастил, надеюсь работает
]