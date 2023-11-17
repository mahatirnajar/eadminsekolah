from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='has_role')
def has_role(user, has_role):
    try:
        roles = has_role.split(',')      
        group = Group.objects.filter(name__in=roles)
        
    except Group.DoesNotExist:
        return False
        
    return any(i in group for i in user.groups.all())