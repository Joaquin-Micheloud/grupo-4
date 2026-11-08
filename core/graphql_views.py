from graphene_django.views import GraphQLView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication


class JWTGraphQLView(GraphQLView):
    """Integración de JWTAuthentication de DRF en GraphQLView."""

    def dispatch(self, request, *args, **kwargs):
        try:
            result = JWTAuthentication().authenticate(request)
        except AuthenticationFailed:
            result = None
        if result is not None:
            request.user, _ = result
        return super().dispatch(request, *args, **kwargs)