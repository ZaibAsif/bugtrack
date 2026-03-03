from django.urls import path
from .views import RegisterView, LoginView, ChangeUserRoleView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/<int:pk>/role/', ChangeUserRoleView.as_view(), name='change-user-role'),
]