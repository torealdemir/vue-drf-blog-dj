from django.urls import path
from blog import views

urlpatterns = [
    path('', views.get_blogs),
    path('<slug:slug>/', views.get_blogd),
]