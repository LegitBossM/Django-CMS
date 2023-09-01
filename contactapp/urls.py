from django.urls import path
from .import views

urlpatterns = [
    path('', views.loginPage, name='login'),
    path('register', views.registerPage, name='register'),
    path('home', views.homePage, name='home'),
    path('addnew', views.addnewPage, name='addnew'),
    path('view', views.viewList, name='view-list'),
    path('search', views.search, name='search'),
    path('logoutPage', views.logoutPage, name='logout'),
]