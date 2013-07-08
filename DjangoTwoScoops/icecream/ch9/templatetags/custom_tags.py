# -*- coding: UTF-8 -*-
import re
from django.utils import timezone

__author__ = 'ielkin'

# Template tag library
# Load it using {% load poll_extras %}

from django import template

register = template.Library()

# Custom tag
# 1. Compilation function
@register.tag(name="my_current_time")
def do_current_time(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, format_string = token.split_contents()
    except ValueError:
        msg = '%r tag requires a single argument' % token.split_contents()[0]
        raise template.TemplateSyntaxError(msg)
    return CurrentTimeNode(format_string[1:-1])


# 2. Render function
class CurrentTimeNode(template.Node):
    def __init__(self, format_string):
        self.format_string = str(format_string)

    def render(self, context):
        now = timezone.datetime.now()
        return now.strftime(self.format_string)


# Sets current time into context variable
@register.tag(name="my_current_time_2")
def do_current_time2(parser, token):
    # This version uses a regular expression to parse tag contents.
    try:
        # Splitting by None == splitting by spaces.
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        msg = '%r tag requires arguments' % token.contents[0]
        raise template.TemplateSyntaxError(msg)

    m = re.search(r'(.*?) as (\w+)', arg)
    if m:
        fmt, var_name = m.groups()
    else:
        msg = '%r tag had invalid arguments' % tag_name
        raise template.TemplateSyntaxError(msg)

    if not (fmt[0] == fmt[-1] and fmt[0] in ('"', "'")):
        msg = "%r tag's argument should be in quotes" % tag_name
        raise template.TemplateSyntaxError(msg)

    return CurrentTimeNode2(fmt[1:-1], var_name)


class CurrentTimeNode2(template.Node):
    def __init__(self, format_string, var_name):
        self.format_string = str(format_string)
        self.var_name = var_name

    def render(self, context):
        now = timezone.datetime.now()
        context[self.var_name] = now.strftime(self.format_string)
        return ''

# As simple tag
@register.simple_tag(name="my_simple_time")
def current_time(format_string):
    try:
        return timezone.datetime.now().strftime(str(format_string))
    except UnicodeEncodeError:
        return ''


# Custom filter
# Use as {{ var|cut:" " }}
@register.filter(name="my_cut")
def cut(value, arg):
    "Removes all values of arg from the given string"
    return value.replace(arg, '')