from django.conf.urls import url, include
from creditcards import urls as creditcards_urls
from addresses import urls as addresses_urls
from users.forms import SignUpForm
from . import views

urlpatterns = [
    url(r'profile/$', views.profile, name='profile'),
    url(r'logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'signup/$',
        views.SignUpView.as_view(form_class=SignUpForm),
        name='signup'),
    url(r'changepassword/$', views.changepassword, name='changepassword'),
    url(r'^creditcards/', include(creditcards_urls)),
    url(r'^addresses/', include(addresses_urls)),
    url('^', include('django.contrib.auth.urls'))
]
