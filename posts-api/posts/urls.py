from django.urls import path

from . import views

urlpatterns = [
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    path('users/', views.ApiRoot.as_view(), name=views.UserList.name),
    path('user-posts/', views.UserPostsList.as_view(), name=views.ApiRoot.name),
    path('post-comments/', views.PostCommentsList.as_view(), name=views.ApiRoot.name),
    path('users/<int:id>', views.UserDetail.as_view(), name=views.UserDetail.name),
    path('posts/<int:id>', views.PostDetail.as_view(), name=views.PostDetail.name),
]