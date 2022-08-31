from .models import Stuff
from .serializers import StuffSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

class StuffList(ListCreateAPIView):
    queryset = Stuff.objects.all()
    serializer_class = StuffSerializer

class StuffDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Stuff.objects.all()
    serializer_class = StuffSerializer