from django.conf.urls import include, url
from . import views

from django.contrib import admin
admin.autodiscover()


# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^sign-in$', views.sign_in , name = 'sign-in'),
    url(r'^sign-up$', views.sign_up , name = 'sign-up'),
    url(r'^authenticate$', views.auth_user , name = 'user_auth'),
]
