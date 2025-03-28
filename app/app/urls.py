from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = ([
                   path('api/admin/', admin.site.urls),
                   path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
                   path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
                   path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
                   path('api/user/', include('users.urls')),
                   path('api/restaurant/', include('restaurant.urls')),
                   path('api/', include('orders.urls'))
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
               static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
