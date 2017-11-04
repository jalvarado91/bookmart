from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
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
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT
                                         }),
] + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT)
