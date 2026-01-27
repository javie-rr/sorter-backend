from rest_framework import viewsets
from rest_framework.response import Response

class BaseViewSet(viewsets.ModelViewSet):
    # Each child view can override this property.
    response_key = 'data'

    """
    Base ViewSet that adds the authenticated user's data
    to all GET responses (list and retrieve).
    """
    def finalize_response(self, request, response, *args, **kwargs):
        response = super().finalize_response(request, response, *args, **kwargs)

        if request.method == 'GET' and isinstance(response.data, (dict, list)):
            group = None
            if request.user.is_authenticated and request.user.groups.exists():
                group = request.user.groups.first().name

            response.data = {
                'user': {
                    'id': request.user.id,
                    'first_name': request.user.first_name, 
                    'last_name': request.user.last_name, 
                    'second_last_name': request.user.second_last_name,
                    'username': request.user.username,
                    'email': request.user.email,
                    'rol': group,
                },
                self.response_key: response.data 
            }

        return response

