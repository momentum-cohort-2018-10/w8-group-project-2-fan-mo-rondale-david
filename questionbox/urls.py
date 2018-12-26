"""questionbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from questions import views
from questions import views as questions_views
from api import urls as api_urls
from django.conf import settings
from django.conf.urls.static import static
from questions.backends import CustomRegistrationView


urlpatterns = [
    path('', views.QuestionListView.as_view(), name='home'),
    path('api/', include(api_urls)),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('accounts/register',
         CustomRegistrationView.as_view(),
         name='registration'),
    path('userprofile/', questions_views.profile, name='profile'),
    path('userprofile/edit/',
         questions_views.edit_profile,
         name='edit_profile'),
    path('change-password/',
         questions_views.change_password,
         name='change_password'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
