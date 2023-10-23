from rest_framework import serializers
from .models import TarifaLuz

#hacer que los modelos sena datos sean solicitados 
class TarifaLuzSerializer(serializers.ModelSerializer):
    class Meta:
        model = TarifaLuz
        fields = '__all__'