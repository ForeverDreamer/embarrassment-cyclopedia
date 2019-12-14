import os
import magic
import random

from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.exceptions import ValidationError

from rest_framework import serializers

# TEMP_DIR = os.path.join(settings.BASE_DIR, 'temp')
TEMP_DIR = 'tmp'


def validate_file_type(upload):
    # Make uploaded file accessible for analysis by saving in tmp
    # tmp_path = '{tmp_dir}/{filename}'.format(tmp_dir=TEMP_DIR, filename=upload.name[2:])
    # python-magic不支持中文路径
    new_filename = str(random.randint(1, 3910209312))
    tmp_path = os.path.join(TEMP_DIR, new_filename)
    default_storage.save(tmp_path, ContentFile(upload.file.read()))
    full_tmp_path = os.path.join(settings.MEDIA_ROOT, tmp_path)
    # exist = os.path.exists(full_tmp_path)
    # Get MIME type of file using python-magic and then delete
    file_type = magic.from_file(full_tmp_path, mime=True)
    # file_type = magic.from_buffer(open(full_tmp_path).read(2048))
    default_storage.delete(tmp_path)
    # Raise validation error if uploaded file is not an acceptable form of media
    # if file_type not in settings.IMAGE_TYPES and file_type not in settings.VIDEO_TYPES:
    if file_type not in settings.VIDEO_TYPES:
        raise serializers.ValidationError('不支持的文件类型，仅支持mp4, avi, mov, wmv, flv文件')
