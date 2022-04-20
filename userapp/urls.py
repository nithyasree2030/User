from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *


urlpatterns = [
    path('api/token_obtain/', TokenObtainPairView.as_view(), name='token_obtain_view'),
    path('api/refresh_view/', TokenRefreshView.as_view(), name='refresh_view'),
    path('api/login_api/', Login.as_view(), name='refresh_view'),
    path('api/user_api/', UserApi.as_view(), name="user_api"),
    path('api/team_api/', TeamApi.as_view(), name="team_api"),
    path('api/team_members_api/', TeamMemberApi.as_view(), name="team_members_api"),
    path('api/task_api/', TaskApi.as_view(), name="task_api"),
    path('api/team_availability/<int:pk>/', TeamAvailability.as_view(), name="team_availability"),
    path('api/task/', TaskCreate.as_view(), name="task_assign"),
    path('api/status_update/', StatusUpdate.as_view(), name="task_status_update"),
    path('api/status_update_user/<int:pk>/', TaskStatusUpdateByUser.as_view(), name="status_update_user"),
]
