# from django.conf import settings
# from datetime import datetime, timedelta
#
#
# def generate_jwt_access_token(username):
#     expiration_time = datetime.now() + timedelta(seconds=settings.JWT_EXPIRATION_SECONDS)
#     payload = {
#         'username': username,
#         'exp': expiration_time,
#         'type': 'access',
#     }
#     return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
#
#
# def generate_jwt_refresh_token(username):
#     expiration_time = datetime.now() + timedelta(days=settings.JWT_EXPIRATION_DAYS)
#     payload = {
#         'username': username,
#         'exp': expiration_time,
#         'type': 'refresh',
#     }
#     return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
#
#
# def decode_jwt_token(token):
#     try:
#         payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
#         return payload
#     except jwt.ExpiredSignatureError:
#         return None  # Token has expired
#     except jwt.InvalidTokenError:
#         return None  # Invalid token
