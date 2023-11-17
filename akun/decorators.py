from audioop import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import messages

def unauthenticated_user(view_func):
    def wrapper_funct(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_funct


def allowed_user(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_funct(request, *args, **kwargs):
            groups = []
            if request.user.groups.exists():
                group = request.user.groups.all()

                for g in group:
                    groups.append(g.name)

            # if group in allowed_roles:
            if (any(el in groups for el in allowed_roles)):
                return view_func(request, *args, **kwargs)
            
            else:
                messages.warning(request, "Anda Tidak Memiliki Akses ke Halaman Ini")
                return redirect('dashboard')

        return wrapper_funct
    return decorator