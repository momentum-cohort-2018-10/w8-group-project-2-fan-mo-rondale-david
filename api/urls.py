from django.urls import path, include
from api import views as api_views


urlpatterns = [
    path('', api_views.api_root),
    path('users/', api_views.UserListView.as_view(), name='user-list'),
    path('users/<pk>/',
         api_views.UserDetailView.as_view(),
         name='user-detail'),
    path('stars/', api_views.StarredItemList.as_view(), name='star-list'),
    path('stars/<pk>',
         api_views.StarredItemDetail.as_view(),
         name='star-detail'),
    path('questions/',
         api_views.QuestionListView.as_view(),
         name='question-list'),
    path('questions/<pk>',
         api_views.QuestionDetailView.as_view(),
         name='question-detail'),
    path('questions/<pk>/answers/',
         api_views.QuestionAnswerList.as_view(),
         name='question-answer-list'),
    path('answers/',
         api_views.AnswerListView.as_view(),
         name='answer-list'),
    path('answers/<pk>',
         api_views.AnswerDetailView.as_view(),
         name='answer-detail'),
]
