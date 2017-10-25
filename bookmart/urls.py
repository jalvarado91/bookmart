"""bookmart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

from users import urls as user_urls
from books import urls as book_urls
from carts import urls as cart_urls
from bookmart.views import HomePageView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include(user_urls, namespace='users')),
    url(r'^carts/', include(cart_urls)),
    url(r'^books/', include(book_urls)),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^resetpassword/$', password_reset, name='resetpassword'),
    url(r'^resetpassworddone/$', password_reset_done,
        name='resetpassworddone'),
    url(r'^resetpasswordconfirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        password_reset_confirm,
        name='resetpasswordconfirm'),
    url(r'^resetpasswordcomplete/$',
        password_reset_complete,
        name='resetpasswordcomplete'),
]
