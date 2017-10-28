from django.conf.urls import url
from addresses.views import addressview
from . import views

urlpatterns = [
    url(r'^$', addressview, name='addresses'),
    url(r'^(?P<address_id>\d+)/$', addressview, name='addressbound'),
]
