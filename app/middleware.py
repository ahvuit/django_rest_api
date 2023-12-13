class SetJsonContentTypeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        excluded_paths = ['/oauth2/token/']

        if not any(request.path.startswith(path) for path in excluded_paths):
            request.META['CONTENT_TYPE'] = 'application/json'
        response = self.get_response(request)
        return response
