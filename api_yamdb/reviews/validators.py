from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_title_year(value):
    if value > timezone.now().year:
        raise ValidationError(
            ('Год выпуска %(value)s больше текущего.'),
            params={'value': value},
        )
