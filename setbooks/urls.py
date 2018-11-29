from django.conf.urls import  url
from . import views

urlpatterns = [
    url(r'^queries/$',views.BookInfoView.as_view()),
    url(r'^options/(?P<pk>\d+)/$',views.BookOptionsView.as_view()),
]