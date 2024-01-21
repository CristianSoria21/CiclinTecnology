from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posiciones.urls')),
    path('posiciones/', include(('posiciones.urls', 'posiciones'), namespace='posiciones')),
    path('accouunts/', include('django.contrib.auth.urls'))

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
