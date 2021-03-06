import hashlib
from urllib.parse import urlencode

from .models import SandstormUser

from urllib.parse import unquote

def remember_sandstorm_user(request):
    sid = request.META.get('HTTP_X_SANDSTORM_USER_ID', "anonym")
    name = unquote(request.META.get('HTTP_X_SANDSTORM_USERNAME', "Anonymous User"))
    handle = request.META.get('HTTP_X_SANDSTORM_HANDLE', "anon")
    gender = request.META.get('HTTP_X_SANDSTORM_PREFERRED_PRONOUNS', "female")
    image_url = request.META.get('HTTP_X_SANDSTORM_USER_PICTURE', None)
    perms = request.META.get('HTTP_X_SANDSTORM_PERMISSIONS', "")
    try:
        u = SandstormUser.objects.get(sid=sid)
        if u.name == name and u.handle == handle and u.gender == gender and u.image_url == image_url:
            return u
        u.name = name
        u.handle = handle
        u.gender = gender
        u.image_url = image_url
        u.save(force_update=True)
    except SandstormUser.DoesNotExist:
        u = SandstormUser(sid=sid,name=name,handle=handle,gender=gender,image_url=image_url)
        u.save(force_insert=True)
    return u

class SandstormUserRemembering:
    def process_request(self, request):
        u = remember_sandstorm_user(request)
        request.sandstorm_user = u
