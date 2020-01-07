from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='blog-home'),
    path('', views.PostList.as_view(), name='blog-home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    # path('about/', views.about, name='blog-about'),
]