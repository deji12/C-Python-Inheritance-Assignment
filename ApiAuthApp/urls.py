from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing),
    path('login/', views.login),
    path('signup/', views.signup),
    path('test-view/', views.TestView),
    path('logout/', views.logout),
]