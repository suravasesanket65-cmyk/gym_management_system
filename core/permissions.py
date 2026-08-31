# pyrefly: ignore [missing-import]
from rest_framework.permissions import BasePermission
from django.conf import settings

class HasAPIKey(BasePermission):
    """
    Allows access only to requests with a valid API Key in the 'X-API-Key' header.
    """
    def has_permission(self, request, view):
        # We look for the 'X-API-Key' header
        api_key = request.META.get('HTTP_X_API_KEY')
        return api_key == getattr(settings, 'API_KEY', None)
