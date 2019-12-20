import json

from django.shortcuts import render
from django.utils.safestring import mark_safe


def index(request):
    return render(request, 'index.html', {})


def group_chat(request):
    return render(request, 'group_chat.html', {
        'group_name_json': mark_safe(json.dumps(request.group_name))
    })


def private_chat(request):
    return render(request, 'private_chat.html', {
        'other_user_json': mark_safe(json.dumps(request.GET.get('user_id')))
    })
