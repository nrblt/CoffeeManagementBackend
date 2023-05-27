from rest_framework.routers import SimpleRouter
from django.urls import path

from .views import AdminViewSet


# app_name = 'admin_app'

# router = SimpleRouter()
# router.register("", AdminViewSet)
# urlpatterns = router.urls
get_position =  AdminViewSet.as_view({'get': 'getPosition'})
today_income =  AdminViewSet.as_view({'get': 'todaysIncome'})

urlpatterns = [
    path('get-position', get_position),
    path('today-income', today_income),

]