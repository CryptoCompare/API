from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/v1/liveData/$', views.liveData.as_view()),
    url(r'^api/v1/History/$', views.history.as_view()),
]