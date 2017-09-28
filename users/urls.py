from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'profile/', views.profile, name='profile'),
    url(r'logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'signup/$', views.SignupView.as_view(), name='signup'),
    url(r'changepassword/$', views.changepassword, name='changepassword'),
    url('^', include('django.contrib.auth.urls'))
]
