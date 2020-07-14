from django import template
import re

register = template.Library()


@register.filter
def is_sig(value):
	var=re.compile(r'/\d/')
	return bool(var.match(value))

@register.filter
def add_value(value, count):
    return value[count-1]

    