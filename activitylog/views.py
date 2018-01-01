from rest_framework_jwt.views import ObtainJSONWebToken

from .serializers import JWTSerializer
# Create your views here.
class ObtainJWTView(ObtainJSONWebToken):
    serializer_class = JWTSerializer
