from django.conf.urls import url, include
from . import views
from carts.views import CartView

urlpatterns = [
    url(r'^$',views.CartView, name = 'CartView'),
]
