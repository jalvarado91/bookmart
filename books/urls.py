from django.conf.urls import url, include
from . import views 
from users import urls as users_urls

app_name = 'books'
urlpatterns = [
    # /books/  this will show a page with all the Books
    url(r'^$', views.index, name='index'),
    # /books/05/ this will show a page with the details od the views
    url(r'(?P<book_id>[0-9]+)/$', views.book_detail, name='detail'),
]
