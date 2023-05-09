from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet

router = DefaultRouter()
router.register("", CategoryViewSet)
app_name = 'category'

urlpatterns = router.urls
