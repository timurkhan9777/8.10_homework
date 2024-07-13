from django.urls import path,include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from .views import UserVideoAPIView

from rest_framework import routers

router = routers.DefaultRouter()
router.register("video",UserVideoAPIView)


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/',include(router.urls)),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('auth/',include('djoser.urls')),
    path('auth/token/',include('djoser.urls.authtoken')),
]