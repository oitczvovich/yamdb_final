from rest_framework import filters, mixins, viewsets

from .pagination import TitleGenreCategoryPagination
from .permissions import IsAdminOrReadOnly


class CreateListDestroyViewset(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = None
    pagination_class = TitleGenreCategoryPagination
    permission_classes = (IsAdminOrReadOnly,)
    search_fields = ('name',)
    lookup_field = 'slug'
    filter_backends = (filters.SearchFilter,)
