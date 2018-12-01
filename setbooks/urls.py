from django.conf.urls import url
from . import views
from rest_framework.routers import DefaultRouter

"""urlpatterns = [
    # url(r'^queries/$',views.BookInfoView.as_view()),
    url(r'^options/(?P<pk>\d+)/$',views.BookOptionsView.as_view()),
    url('^books/$', views.BookView.as_view()),
    url('^heros/$', views.HeroView.as_view())
]
# 定义可以处理视图的路由器
router = DefaultRouter()
# 向路由器注册视图集
router.register(r'queries', views.BookInfoViewSet)
urlpatterns += router.urls
"""
urlpatterns = [
    url(r'^books/$',views.BookView.as_view()),
    url(r'^books/(?P<pk>\d+)/$', views.BooksView.as_view()),
    url(r'^heros/$',views.HerosView.as_view()),
    # url(r'^heros/(?P<pk>\d+)$',views.HeroView.as_view()),
]
