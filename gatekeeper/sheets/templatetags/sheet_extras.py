from django import template
from ..models import Sheet

register = template.Library()

@register.simple_tag
def skill(id, stat, name):
    sheet = Sheet.objects.get(id=id)
    proficient = eval('sheet.' + name)
    # exec('proficient = sheet.' + name)
    proficientBonus = sheet.proficiency
    value = ''

    tempValue = eval('sheet.' + stat + 'Mod')
    # exec('tempValue = sheet.' + stat + 'Mod')
    if proficient:
        tempValue += proficientBonus
    
    if tempValue >= 0:
        value = '+ ' + str(tempValue)
    else:
        value = '' + str(tempValue)
    
    return value


@register.simple_tag
def saving_throw(id, stat):
    sheet = Sheet.objects.get(id=id)
    proficient = eval('sheet.s' + stat[0].upper() + stat[1:])
    proficientBonus = sheet.proficiency

    tempValue = eval('sheet.' + stat + 'Mod')
    if proficient:
        tempValue += proficientBonus
    
    if tempValue >= 0:
        value = '+ ' + str(tempValue)
    else:
        value = '' + str(tempValue)
    
    return value


@register.simple_tag
def item(strength, prof, isProf):
    tempValue = strength
    if isProf:
        tempValue += prof
    
    if tempValue >= 0:
        value = '+ ' + str(tempValue)
    else:
        value = '' + str(tempValue)

    return value
