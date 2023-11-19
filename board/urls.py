from django.urls import path, include
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from board.views import BoardAPIView

router = routers.DefaultRouter()
router.register(r'', BoardAPIView)

urlpatterns = [
    path('', include(router.urls))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
