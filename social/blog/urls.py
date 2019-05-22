from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UploadListView,
    UploadDetailView,
    UploadCreateView,
    UploadUpdateView,
    UploadDeleteView

)
from . import views

urlpatterns = [
    #path('',views.home,name='blog-home'),
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('search/',views.search,name='blog-search'),
    path('upload/',UploadListView.as_view(),name='upload'),
    path('upload/<int:pk>/', UploadDetailView.as_view(), name='upload-detail'),
    path('upload/new/', UploadCreateView.as_view(), name='upload-create'),
    path('upload/<int:pk>/update/', UploadUpdateView.as_view(), name='upload-update'),
    path('upload/<int:pk>/delete/', UploadDeleteView.as_view(), name='upload-delete'),
    path('timeline/<int:pk>',views.timeline,name='timeline')
]