from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

# router object
router = DefaultRouter()

# register a new url with the router than points to the HelloViewSet
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
# register viewset with a url
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, base_name='login')


# url-dispatcher
# api/hello-view/
urlpatterns = [
    # return as a view object
    url(r"^hello-view/", views.HelloApiView.as_view()),
    url(r'', include(router.urls))
]
