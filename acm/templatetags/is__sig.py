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


@register.filter
def is_core_sig(value):
    return value <= 4

@register.filter
def is_main_sig(value):
    return int(value) <= 5
