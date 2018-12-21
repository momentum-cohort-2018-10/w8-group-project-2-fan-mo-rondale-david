from django.urls import path, include
from api import views as api_views


urlpatterns = [
    path('', api_views.api_root),
    path('api-auth/', include('rest_framework.urls')),
    path('users/', api_views.UserListView.as_view(), name='user-list'),
    path('myquestions/',
         api_views.UserQuestionListView.as_view(),
         name='author-question-list'),
    path('myanswers/',
         api_views.UserAnswerListView.as_view(),
         name='author-answer-list'),
    path('users/<pk>/',
         api_views.UserDetailView.as_view(),
         name='user-detail'),
    path('users/<pk>/questions/',
         api_views.QuestionsByUserListView.as_view(),
         name='question-list-by-user'),
    path('users/<pk>/answers/',
         api_views.AnswersByUserListView.as_view(),
         name='answer-list-by-user'),
    path('stars/<pk>',
         api_views.StarredItemDetail.as_view(),
         name='star-detail'),
    path('questions/',
         api_views.QuestionListView.as_view(),
         name='question-list'),
    path('questions/<pk>/',
         api_views.QuestionDetailView.as_view(),
         name='question-detail'),
    path('questions/<pk>/answers/',
         api_views.QuestionAnswerList.as_view(),
         name='question-answer-list'),
    path('questions/<pk>/stars/',
         api_views.QuestionStarList.as_view(),
         name='question-star-list'),
    path('answers/<pk>/',
         api_views.AnswerDetailView.as_view(),
         name='answer-detail'),
    path('answers/<pk>/stars/',
         api_views.AnswerStarList.as_view(),
         name='answer-star-list'),
]
