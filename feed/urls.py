from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]