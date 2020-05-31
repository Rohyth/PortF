from django.urls import path, include
from rest_framework import routers
from .views import scrapper1, HeroViewSet


router = routers.DefaultRouter()
router.register(r'heroes', HeroViewSet)

urlpatterns = [
    # path('', scrapper1, name='Scrapper1'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]



