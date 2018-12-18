from django.urls import path, include
from rest_framework import routers
from questions import views as api_views


urlpatterns = [
    path('users/', api_views.UserListView.as_view(), name='user-list'),
    path('users/<pk>/',
         api_views.UserDetailView.as_view(),
         name='user-detail'),
    path('stars/', api_views.StarredItemList.as_view(), name='star-list'),
    path('questions/',
         api_views.QuestionListView.as_view(),
         name='question-list'),
]
