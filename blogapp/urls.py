from django.urls import path
from blogapp import views

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('blog-detail/<str:slug>/', views.ArticleDetail, name='detail'),
]