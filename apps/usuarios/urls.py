from django.urls import path, include
from rest_framework import routers
from .views import LoginView, RegisterView
from apps.usuarios import views

router = routers.DefaultRouter()

router.register(r'agente', views.AgenteViewSet)

urlpatterns = [
    path('api/', include(router.urls)),    
        # Auth views
    path('api/auth/login/',LoginView.as_view(), name='auth_login'),
    path('api/register/', RegisterView.as_view(), name='auth_register'),

    # path('auth/logout/',LogoutView.as_view(), name='auth_logout'),
]