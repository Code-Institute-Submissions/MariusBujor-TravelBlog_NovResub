from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('post/new/', views.CreatePostView.as_view(), name='post_create'),
    # path('<slug:slug>/update/', views.UpdatePostView.as_view(), name='post-update'),
]
