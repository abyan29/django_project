from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required

def admin_required(view_func):
    @login_required
    def wrapper(request, *args, **kwargs):
        if request.user.role != 'admin':
            raise PermissionDenied("Kamu tidak punya akses ke halaman ini.")
        return view_func(request, *args, **kwargs)
    return wrapper
