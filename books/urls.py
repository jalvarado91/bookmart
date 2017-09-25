from django.conf.urls import url, include
<<<<<<< HEAD
from . import views #line added by lida

urlpatterns = [
    # /books/  this will show a page with all the Books
    url(r'^$',views.index, name = 'index'),

    # /books/05/ this will show a page with the details od the views
    url(r'(?P<book_id>[0-9]+)/$', views.book_detail, name = 'detail'),
]
=======
from users import urls as users_urls

urlpatterns = [
    
]
>>>>>>> c152504a46e558e1b2f18d4e76ac8f9e6bcddb51
