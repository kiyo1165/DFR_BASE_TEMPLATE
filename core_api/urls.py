from django.urls import path, include
from rest_framework import routers
from . import views

app_name = "core_api"
router = routers.DefaultRouter()

router.register('message', views.MessageViewSet)
router.register('profile', views.ProfileViewSet)

urlpatterns = [
    path('create_user/', views.CreateUserView.as_view(), name="create_user"),
    path('users/', views.ListUserView.as_view(), name="users"),
    path('user/', views.LoginUserView.as_view(), name="user"),
    path('inbox/', views.InboxListViewSet.as_view(), name="inbox"),
    path('', include(router.urls)),

]
