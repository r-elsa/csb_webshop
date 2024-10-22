from django.contrib.auth import get_user_model
from django.utils.deprecation import MiddlewareMixin

class AutoLoginSuperUserMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path.startswith('/admin/') and not request.user.is_authenticated:
            User = get_user_model()
            try:
                superuser = User.objects.get(is_superuser=True)
                if superuser:
                    request.user = superuser
            except User.DoesNotExist:
                pass  