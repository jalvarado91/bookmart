from django.conf.urls import url
from . import views

app_name = 'carts'
urlpatterns = [
    url(r'^$', views.detail, name='detail'),
    url(r'^add/(?P<book_id>\d+)/$', views.cart_add, name='add'),
    url(r'^remove/(?P<book_id>\d+)/$', views.cart_remove, name='cart_remove'),
    ]
