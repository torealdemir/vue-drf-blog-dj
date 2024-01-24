from django.urls import path
from blog import views
from rest_framework import routers
from . import views
from .models import Blog
# urlpatterns = [
#     path('', views.get_blogs),
#     path('<slug:slug>/', views.get_blogd),
#     path('addblog/', views.add_blog),
#     path('notes/', views.NoteViewset.as_view({'post': 'note'}), name='notes'),
# ]


router = routers.DefaultRouter()
##router.register('addblog/', views.BlogCreateAPIView, basename="tore")
router.register('', views.BlogListViewset, basename="tore1")
##router.register('<slug:slug>', views.BlogDetailViewset, basename="tore2")

urlpatterns = [
    path('addblog/', views.BlogCreateAPIView.as_view())
]

urlpatterns += router.urls