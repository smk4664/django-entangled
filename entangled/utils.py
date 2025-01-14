from django.apps import apps
from django.db.models import ObjectDoesNotExist


def get_related_object(scope, field_name):
    """
    Returns the related field, referenced by the content of a ModelChoiceField.
    """
    try:
        Model = apps.get_model(scope[field_name]['model'])
        relobj = Model.objects.get(pk=scope[field_name]['pk'])
    except (ObjectDoesNotExist, LookupError):
        relobj = None
    return relobj


def get_related_queryset(scope, field_name):
    """
    Returns the related queryset, referenced by the content of a ModelChoiceField.
    """
    try:
        Model = apps.get_model(scope[field_name]['model'])
        queryset = Model.objects.filter(pk__in=scope[field_name]['p_keys'])
    except LookupError:
        queryset = None
    return queryset
