from django.conf.urls import  url
from . import views

urlpatterns = [
    url(r'^query/$',views.BookInfoView.as_view()),
]