from django import template

register = template.Library()


@register.filter
def currentLife(cuurLife):
    per = cuurLife * 100 / 2000 
    return per