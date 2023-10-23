from rest_framework import routers
from .api import TarifasViewset

router = routers.DefaultRouter()
router.register('Tarifas', TarifasViewset,'Tarifas')

urlpatterns= router.urls