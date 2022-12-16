from rest_framework.routers import SimpleRouter

from .views import CartItemViewSet

router = SimpleRouter()
router.register("",CartItemViewSet)
urlpatterns = router.urls
