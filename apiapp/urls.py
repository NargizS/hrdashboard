from django.conf.urls import include, url
from rest_framework import routers
from apiapp import views as apiviews

router = routers.DefaultRouter() 
router.register(r'users', apiviews.UserViewSet) 
router.register(r'profile', apiviews.ProfileViewSet)

urlpatterns = [ 
	url(r'^', include(router.urls, namespace='api')), 
    url(r'^api-auth/', include('rest_framework.urls')),
]


