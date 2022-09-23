from django.urls import path, include
from apps.usuarios import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'perfil', views.PerfilViewSet)

urlpatterns = [
    path('api/', include(router.urls)),    
]