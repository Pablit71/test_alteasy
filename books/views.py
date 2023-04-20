from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Profile, Book
from .serializers import BookSerializer, ProfileSerializer


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def list(self, request, *args, **kwargs):
        # Получаем все видимые столбцы из профилей
        visible_columns = Profile.objects.filter(is_visible=False).values_list('column_name', flat=True)
        # Получаем все видимые профили
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.exclude(column_name__in=visible_columns)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

