from django.conf.urls import url
from . import views

urlpatterns = [
    url('^edit/$',views.edit_profile, name="edit_profile"),
    # url('^account/(?P<username>[a-zA-Z0-9]+)$', views.get_user_profile),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='view_profile_with_pk'),
]