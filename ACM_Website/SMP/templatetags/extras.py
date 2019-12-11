from django import template

register = template.Library()


@register.filter
def to_str(value):
    return str(value)


@register.simple_tag
def concatenate(a, b, c):
    return a+str(b) + c
