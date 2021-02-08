from django import template

register = template.Library()


@register.filter
def currentLife(cuurLife):
    per = cuurLife * 100 / 2000 
    return per


@register.filter
def dmgPer(dmg, curr_dmg):
    per =  dmg * 100 // (2000 - curr_dmg)
    return per
