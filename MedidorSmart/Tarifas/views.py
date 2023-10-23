from rest_framework import generics
from .models import TarifaLuz
from .serializers import TarifaLuzSerializer

class TarifaLuzList(generics.ListCreateAPIView):
    queryset = TarifaLuz.objects.all()
    serializer_class = TarifaLuzSerializer

class TarifaLuzDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TarifaLuz.objects.all()
    serializer_class = TarifaLuzSerializer
