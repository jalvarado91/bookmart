from django.conf.urls import url, include
from creditcards.views import creditcardview

urlpatterns = [
    url(r'^creditcards/$', creditcardview, name='creditcards'),
    url(r'^creditcards/(?P<creditcard_id>\d+)/$',
        creditcardview,
        name='creditcardbound'),
]
