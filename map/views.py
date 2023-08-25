from rest_framework import generics
from map.models import Objects
from map.serializers import ObjectSerializer



class ObjectApiView(generics.ListAPIView):
    queryset = Objects.objects.all()
    serializer_class = ObjectSerializer

    
