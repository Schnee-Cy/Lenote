# -*- coding: utf-8 -*-

import markdown
import markdownx
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe
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



@register.filter(is_safe = True)
@stringfilter
def custom_markdown(value):
    return mark_safe(markdown.markdown(value,
                              extensions = ['markdown.extensions.extra',
											'markdown.extensions.toc',
											'markdown.extensions.sane_lists',
											'markdown.extensions.nl2br',
                                            'markdown.extensions.codehilite'],
                              safe_mode = True,
                              enable_attributes = False))

