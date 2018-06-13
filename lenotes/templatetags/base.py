# -*- coding: utf-8 -*-

from django import template
from users.models import UserInfo
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()

@register.filter
def getUnreadCount(user):
    try:
        info = UserInfo.objects.get(user=user)
    except ObjectDoesNotExist:
        return 0
    else:
        return info.unread_count