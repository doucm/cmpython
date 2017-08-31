from rest_framework import routers

from .api import OrdersViewSet
router = routers.SimpleRouter()

router.register(r'^', OrdersViewSet, base_name="orders")