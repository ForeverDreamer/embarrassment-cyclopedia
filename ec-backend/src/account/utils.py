import re

from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


def is_phone(phone):
    pattern = re.compile(r'^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$')
    result = re.search(pattern, phone)
    if result:
        return True
    else:
        return False


def is_veri_code(veri_code):
    return True


def validate_openid(openid):
    if len(openid) < 30:
        return False
    return True


# 数字字母下划线
def validate_password(password):
    return True


def validate_third_type(third_type):
    return True

