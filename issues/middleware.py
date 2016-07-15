from .models import SandstormUser

from urllib.parse import unquote

def remember_sandstorm_user(request):
    sid = request.META.get('HTTP_X_SANDSTORM_USER_ID', "anonym")
    name = unquote(request.META.get('HTTP_X_SANDSTORM_USERNAME', "Anonymous User"))
    handle = request.META.get('HTTP_X_SANDSTORM_HANDLE', "anon")
    gender = request.META.get('HTTP_X_SANDSTORM_PREFERRED_PRONOUNS', "female")
    try:
        u = SandstormUser.objects.get(sid=sid)
        u.name = name
        u.handle = handle
        u.gender = gender
    except SandstormUser.DoesNotExist:
        u = SandstormUser(sid=sid,name=name,handle=handle,gender=gender)
    u.save()
    return u

class SandstormUserRemembering:
    def process_request(self, request):
        u = remember_sandstorm_user(request)
        request.sandstorm_user = u
