import datetime
from django.conf import settings
from django.contrib.auth import logout

# ini fungsi nya kalau user idle selama 5 menit 
class AutoLogoutMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            return self.get_response(request)
        
        current_datetime = datetime.datetime.now()
        last_activity = request.session.get('last_activity')

        if last_activity:
            elapsed_time = (current_datetime - datetime.datetime.fromisoformat(last_activity)).seconds
            if elapsed_time > getattr(settings, "AUTO_LOGOUT_DELAY", 300):  # default 5 menit
                logout(request)

        request.session['last_activity'] = current_datetime.isoformat()

        return self.get_response(request)
        
    