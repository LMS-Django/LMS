from django.core.exceptions import ValidationError


class NoDataError(ValidationError):
    pass


class ExessDataError(ValidationError):
    pass