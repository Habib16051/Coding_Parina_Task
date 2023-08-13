from django.urls import path
from . import views


urlpatterns = [
    path('khoj-search/', views.KhojSearchView.as_view(), name='khoj_search'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

]
