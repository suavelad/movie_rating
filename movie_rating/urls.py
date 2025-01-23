from django.urls import include, path
from rest_framework import routers
from . import views

app_name = 'movies'

router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet)
router.register(r'ratings', views.RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]