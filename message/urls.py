from django.urls import path, include
from rest_framework import routers
from message.views import MessageViewSet

router = routers.DefaultRouter()
router.register(r'', MessageViewSet)

urlpatterns = [
    path('api/messages/', include(router.urls))
]