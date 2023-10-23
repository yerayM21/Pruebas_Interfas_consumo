from .models import TarifaLuz
from rest_framework import viewsets, permissions
from .serializers import TarifaLuzSerializer

class TarifasViewset(viewsets.ModelViewSet ):
   #conjunto de datos 
    queryset = TarifaLuz.objects.all()
    #cualquier personas puede soliciar
    permission_classes = [permissions.AllowAny ]
    # como la va converir desde donde 
    serializer_class = TarifaLuzSerializer