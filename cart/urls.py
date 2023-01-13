from rest_framework.routers import SimpleRouter

from .views import CartItemViewSet, CartViewSet

router = SimpleRouter()
router.register("item",CartItemViewSet)
router.register("", CartViewSet)
urlpatterns = router.urls
