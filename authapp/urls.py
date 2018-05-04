from django.conf.urls import include, url
from authapp import views
urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name="home"),
    url(r'^register/$', views.RegisterFormView.as_view(), name='register'),
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^statistics', views.StatisticsView.as_view(), name='statistics'),
    url(r'^applications', views.AppView.as_view(), name='applications'),
]