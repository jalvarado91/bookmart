from django.conf.urls import url, include
from addresses.views import AddressDetailView, AddressesListView
from . import views

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$',
        AddressDetailView.as_view(),
        name='addresses-detail'),
    url(r'^$', AddressesListView.as_view(), name='addresses-list'),
]
