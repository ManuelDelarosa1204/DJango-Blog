from django.db.models import Model


def get_model_field_label(model: Model, field: str) -> str:
    """
    Returns the `label` (verbose name) of the model field

    :param model: The model you want to get a field from
    :type model: Model
    :param field: The field you want to get the label from
    :type field: str
    :rtype: str
    :returns: The verbose name of the model field
    """
    return model._meta.get_field(field).verbose_name
