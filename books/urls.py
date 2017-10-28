from django.conf.urls import url, include
from . import views
from users import urls as users_urls

app_name = 'books'
urlpatterns = [
    # /books/  this will show a page with all the Books
    url(r'^$', views.book_list, name='index'),

    # /books/05/ this will show a page with the details od the views
    url(r'author/(?P<author_id>[0-9]+)/$',
        views.author_list,
        name='author_books'),
    url(r'(?P<book_id>[0-9]+)/$', views.book_detail, name='detail'),
    url(r'(?P<book_id>[0-9]+)/review$', views.book_review, name='review'),
]
