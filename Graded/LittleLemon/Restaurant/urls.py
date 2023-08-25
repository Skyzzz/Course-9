from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>/', views.SingleItemView.as_view()),
    path('users/', views.UserListView.as_view()),
    path('users/<int:pk>/', views.UserDetaiView.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),

]
