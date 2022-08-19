"""Alcheringa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path,include
from users import views as user_views
from AlcherWeb.views import PostListView,PostCreateView
from AlcherWeb import views as Web_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',PostListView.as_view(),name='AlcherWeb-home'),
    path('createview/',PostCreateView.as_view(),name='post-create'),
    path('fav/<int:id>/',user_views.favourite_add,name="favourite_add"),
    path('saved_posts/',user_views.favourite_list, name='favourite_list'),
    path('',user_views.register,name='AlcherWeb-urls-login'),
    path('profile/',user_views.profile,name='profile'),
    path('newpost/',user_views.newpost,name='newpost'),
    path('mypost/', Web_views.myposts, name='mypost'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)