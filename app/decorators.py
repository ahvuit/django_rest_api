# decorators.py
from django.http import JsonResponse
from .jwt_utils import decode_jwt_token


def jwt_required(view_func):
    def wrapper(request, *args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return JsonResponse({'error': 'Token is missing'}, status=401)

        decoded_payload = decode_jwt_token(token)

        if not decoded_payload:
            return JsonResponse({'error': 'Invalid token'}, status=401)

        request.user_id = decoded_payload.get('user_id')
        return view_func(request, *args, **kwargs)

    return wrapper
