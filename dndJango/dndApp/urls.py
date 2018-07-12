from django.conf.urls import url
from .views import TeamList, LevelList, ProductList, ChannelList, PayperiodList, ComponentList
from rest_framework.urlpatterns import format_suffix_patterns
from dndApp import views

urlpatterns = [
    url(r'^team/', views.TeamList.as_view()),
    url(r'^level/', views.LevelList.as_view()),
    url(r'^product/', views.ProductList.as_view()),
    url(r'^channel/', views.ChannelList.as_view()),
    url(r'^payperiod/', views.PayperiodList.as_view()),
    url(r'^component/', views.ComponentList.as_view()),
]
