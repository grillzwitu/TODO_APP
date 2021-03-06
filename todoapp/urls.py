"""todoapp URL Configuration

Copied from todo_app project folder

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('index', views.index, name='index'),
    path('user', views.user, name='user'),
    path('profile', views.profile, name='profile'),
    path('edit', views.edit, name='edit'),
    path('log', views.log, name='log'),
    path('sign', views.sign, name='sign'),
    path('add_task', views.add_task, name='add_task'),
    path('delete_task', views.delete_task, name='delete_task'),
    path('edit_task', views.edit_task, name='edit_task')
]
