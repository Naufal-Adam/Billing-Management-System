from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    return value * arg

def multiply_and_add(value, arg1, arg2):
    return value * arg1 + arg2