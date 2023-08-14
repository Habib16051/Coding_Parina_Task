from django.urls import path
from . import views


urlpatterns = [
    path('input-values/', views.InputValueListCreateAPIView.as_view(),
         name='input_value_list'),
    path('input-values/<int:pk>/',
         views.InputValueRetrieveUpdateDestroyAPIView.as_view(), name='input_value_detail'),


]
