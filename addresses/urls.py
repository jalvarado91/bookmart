from django.conf.urls import url
from addresses.views import AddressDetailView, AddressesListView, addressview
from . import views

urlpatterns = [
    url(r'addresses/$', addressview, name='addresses'),
    url(r'^(?P<slug>[-\w]+)/$',
        AddressDetailView.as_view(),
        name='addresses-detail'),
    url(r'^$', AddressesListView.as_view(), name='addresses-list'),
]
