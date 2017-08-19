from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^liveData/$', views.liveData.as_view()),
    url(r'^History/$', views.history.as_view()),
]