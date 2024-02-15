from django.urls import path
from blog import views
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('', views.BlogListViewset, basename="all-blogs")

urlpatterns = [
    path('addblog/', views.BlogCreateAPIView.as_view())
]

urlpatterns += router.urls