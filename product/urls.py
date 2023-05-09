from rest_framework.routers import SimpleRouter

from .views import  ProductViewSet

app_name = 'product'

router = SimpleRouter()
router.register("",ProductViewSet)
urlpatterns = router.urls
