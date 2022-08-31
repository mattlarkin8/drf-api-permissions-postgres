from .models import Stuff
from .serializers import StuffSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

class StuffList(ListCreateAPIView):
    queryset = Stuff.objects.all()
    serializer_class = StuffSerializer

class StuffDetail(RetrieveUpdateDestroyAPIView):
    queryset = Stuff.objects.all()
    serializer_class = StuffSerializer