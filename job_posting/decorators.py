from django.contrib.auth.models import User
from django.shortcuts import redirect


def redirect_on_user_roles(allowed_group):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if request.user.groups.all()[0].name == allowed_group:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('home')
        return wrapper
    return decorator




