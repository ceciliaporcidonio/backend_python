from rest_framework.routers import DefaultRouter
from .viewsets import ProductViewSet  # Certifique-se de que este import existe

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = router.urls

