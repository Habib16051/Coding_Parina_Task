from django.urls import path
from . import views
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenVerifyView
# )

urlpatterns = [
    path('input-values/', views.InputValueListCreateAPIView.as_view(),
         name='input_value_list'),
    path('input-values/<int:pk>/',
         views.InputValueRetrieveUpdateDestroyAPIView.as_view(), name='input_value_detail'),
    #     path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #     path('refresh_token/', TokenRefreshView.as_view(), name='token_refresh'),
    #     path('verify_token/', TokenVerifyView.as_view(), name='token_verify'),

]
