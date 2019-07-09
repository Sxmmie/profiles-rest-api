from django.conf.urls import url

from . import views


# url-dispatcher
# api/hello-view/
urlpatterns = [
    # return as a view object
    url(r"^hello-view/", views.HelloApiView.as_view())
]
