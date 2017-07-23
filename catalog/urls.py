from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^liveData/(?P<siteId>[0-9]+)/(?P<currency>[A-Z]+)/$', views.liveData.as_view()),

]