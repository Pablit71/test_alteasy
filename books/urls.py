from django.urls import path, include
from rest_framework.routers import DefaultRouter

from books.views import BookViewSet, ProfileViewSet

router = DefaultRouter()
# Регистрируем представления BookViewSet и ProfileViewSet в роутере
router.register(r'books', BookViewSet)
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    # Включаем URL-паттерны роутера
    path('', include(router.urls)),
]
