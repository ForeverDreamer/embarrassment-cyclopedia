from django.core.exceptions import ValidationError

from .utils import is_phone


def validate_mobile_phone(phone):
    if not is_phone(phone):
        raise ValidationError('请输入正确的电话号码！')
    return phone
