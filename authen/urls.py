from django.contrib import admin
from django.urls import path, include

from mysite.core import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]
