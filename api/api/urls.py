from django.contrib import admin
from django.urls import path, include
from core.views import ChannelViewSet, EventViewSet, ProgramViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'channels', ChannelViewSet)
router.register(r'events', EventViewSet)
router.register(r'programs', ProgramViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))   
]
