from django.conf.urls import url
from addresses.views import addressview
from . import views

urlpatterns = [
    url(r'^addresses/$', addressview, name='addresses'),
    url(r'^addresses/(?P<address_id>\d+)/$', addressview, name='addressbound'),
]
