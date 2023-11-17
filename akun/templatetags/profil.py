from django import template
from django.contrib.auth.models import User
from akun.models import *
register = template.Library()
@register.simple_tag(takes_context=True)
def get_profil_user(context):
    request = context['request']
    user=request.user
    try:
        jk=user.jk
    except:
        jk=''
    if jk=='Laki-laki':
        profil='media/avatars/dosen-l.png'
    elif jk == 'perempuan':
        profil='media/avatars/dosen-p.png'
    else:
        profil='media/avatars/dosen-l.png'
    return profil