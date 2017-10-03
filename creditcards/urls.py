from django.conf.urls import url, include
from creditcards.views import CreditCardDetailView, CreditCardListView
from . import views

urlpatterns = [
    url(r'creditcards/$', views.creditcardview, name='creditcards'),
    url(r'^(?P<pk>\d+)/$',
        CreditCardDetailView.as_view(),
        name='creditcards-detail'),
    url(r'^$', CreditCardListView.as_view(), name='creditcards-list'),
]
