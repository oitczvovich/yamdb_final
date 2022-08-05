from rest_framework.pagination import PageNumberPagination


class TitleGenreCategoryPagination(PageNumberPagination):
    """Паджинатор для моделей Title, Genre, Category."""

    page_size = 5
