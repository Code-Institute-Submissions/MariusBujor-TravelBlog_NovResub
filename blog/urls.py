from . import views
from django.urls import path
from.views import CreatePostView, UpdatePostView, DeletePostView
# from wish import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    # path('', include('wish.urls')),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('post/new/', views.CreatePostView.as_view(), name='post_create'),
    # path('wish/new/', views.WishPostView.as_view(), name='post_wish'),
    path('<slug:slug>/update/', UpdatePostView.as_view(), name='post-update'),
    path('<slug:slug>/delete/', DeletePostView.as_view(), name='post-delete'),
    
]
