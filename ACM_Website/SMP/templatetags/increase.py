from django import template

register = template.Library()

@register.filter
def compare(value,count):
	if value[count-1].sub_heading==value[count].sub_heading :
		return 1
	else:
		return 0