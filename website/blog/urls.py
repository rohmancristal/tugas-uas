from django.urls import path

from . import views

urlpatterns = [
    path('', views.blogs),
    path('blogsdetail/<int:id>/', views.blogsdetail, name='detail'),
]