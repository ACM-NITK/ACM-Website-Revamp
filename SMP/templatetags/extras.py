from django import template

register = template.Library()


@register.filter
def to_str(value):
    return str(value)


@register.simple_tag
def concatenate(a, b, c):
    return a+str(b) + c


@register.filter
def compare(value, count):
    if value[count-1].sub_heading == value[count].sub_heading:
        return 1
    else:
        return 0
