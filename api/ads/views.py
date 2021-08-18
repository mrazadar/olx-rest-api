from django.contrib.auth.models import User
from rest_framework import viewsets
# from rest_framework import permissions
from api.ads.models import Ad
from api.ads.serializers import AdSerializer


class AdViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

