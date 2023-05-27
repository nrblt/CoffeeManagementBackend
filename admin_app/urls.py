from rest_framework.routers import SimpleRouter
from django.urls import path

from .views import AdminViewSet


# app_name = 'admin_app'

# router = SimpleRouter()
# router.register("", AdminViewSet)
# urlpatterns = router.urls
get_position =  AdminViewSet.as_view({'get': 'getPosition'})
urlpatterns = [
    path('get-position', get_position),
]