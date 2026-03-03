"""
Custom auth that accepts both "Token <key>" and raw "<key>" in the Authorization header,
so Swagger UI works when users paste only the token.
"""
from rest_framework.authentication import TokenAuthentication as DRFTokenAuthentication


class TokenAuthentication(DRFTokenAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        if auth_header and not auth_header.strip().lower().startswith(self.keyword.lower()):
            request.META["HTTP_AUTHORIZATION"] = f"{self.keyword} {auth_header.strip()}"
        return super().authenticate(request)
