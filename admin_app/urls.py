from rest_framework.routers import SimpleRouter
from django.urls import path

from .views import AdminViewSet


# app_name = 'admin_app'

# router = SimpleRouter()
# router.register("", AdminViewSet)
# urlpatterns = router.urls
get_position =  AdminViewSet.as_view({'get': 'getPosition'})
get_incomes =  AdminViewSet.as_view({'get': 'getIncomes'})
get_paid_orders =  AdminViewSet.as_view({'get': 'getPaidOrders'})

urlpatterns = [
    path('get-position', get_position),
    path('get-incomes', get_incomes),
    path('get-paid-orders', get_paid_orders),
]