from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^liveData/$', views.liveData.as_view()),
    url(r'^History/(?P<siteId>[0-9]+)/(?P<currency>[A-Z]+)/(?P<time>[0-9]+)/$', views.History.as_view()),
]