from django.urls import path, include
from rest_framework import routers
from questions import views as api_views
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('', api_views.api_root),
    path('users/', api_views.UserListView.as_view(), name='user-list'),
    path('users/<pk>/',
         api_views.UserDetailView.as_view(),
         name='user-detail'),
    path('stars/', api_views.StarredItemList.as_view(), name='star-list'),
    path('stars/<pk>', api_views.StarredItemDetail.as_view(), name='star-detail'),
    path('questions/',
         api_views.QuestionListView.as_view(),
         name='question-list'),
]
