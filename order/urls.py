from rest_framework import routers

from order.views import TicketViewSet, OrderViewSet


app_name = "order"


router = routers.DefaultRouter()
router.register("order", OrderViewSet)
router.register("ticket", TicketViewSet)


urlpatterns = [] + router.urls
