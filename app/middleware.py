from django.http import HttpResponseForbidden


class SetJsonContentTypeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        excluded_paths = ['/token/']

        if not any(request.path.startswith(path) for path in excluded_paths):
            request.META['CONTENT_TYPE'] = 'application/json'
        response = self.get_response(request)
        return response


# class SuperuserCheckMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         excluded_paths = ['/oauth2/token/']
#         # Check if the user is a superuser
#         if request.user and not request.user.is_superuser:
#             return HttpResponseForbidden("Permission denied: You must be a superuser.")
#
#         response = self.get_response(request)
#         return response
