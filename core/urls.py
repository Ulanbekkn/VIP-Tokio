import requests.utils
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView, TokenObtainPairView

from core.settings.base import MEDIA_URL, MEDIA_ROOT
from .settings import swagger


urlpatterns = [
    path('admin/', admin.site.urls),

    # models
    path('api/v1/models/', include('apps.models.urls')),
    # others
    path('api/v1/others/', include('apps.others.urls')),
    # users
    path('api/v1/users/', include('apps.users.urls')),

]

urlpatterns += swagger.urlpatterns
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)


