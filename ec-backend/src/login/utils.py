import re


def is_phone(phone):
    pattern = re.compile(r'^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$')
    result = re.search(pattern, phone)
    if result:
        return True
    else:
        return False
