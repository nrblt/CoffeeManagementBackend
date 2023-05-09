from rest_framework.routers import SimpleRouter

from .views import OrderViewSet


app_name = 'order'

router = SimpleRouter()
router.register("", OrderViewSet)
urlpatterns = router.urls
