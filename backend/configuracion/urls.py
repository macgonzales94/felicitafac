"""
Configuración principal de URLs - FELICITAFAC
Sistema de Facturación Electrónica para Perú
Optimizado para MySQL y hosting compartido
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

# Importar vistas desde el archivo views.py
from .views import (
    api_root_view,
    health_check_view,
    info_sistema_view,
    error_404,
    error_500,
    error_403,
    error_400
)


# Configuración principal de URLs
urlpatterns = [
    # Panel de administración Django
    path('admin/', admin.site.urls),
    
    # API raíz - Vista principal del sistema
    path('', api_root_view, name='api-root'),
    path('api/', api_root_view, name='api-root-alt'),
    
    # Health check y información del sistema
    path('health/', health_check_view, name='health-check'),
    path('api/health/', health_check_view, name='api-health-check'),
    path('info/', info_sistema_view, name='info-sistema'),
    path('api/info/', info_sistema_view, name='api-info-sistema'),
    
    # Autenticación
    path('api/auth/token/', obtain_auth_token, name='api-token-auth'),
    path('api/auth/', include('rest_framework.urls')),
    
    # APIs de aplicaciones (implementadas en Fase 1)
    path('api/core/', include('aplicaciones.core.urls')),
    path('api/usuarios/', include('aplicaciones.usuarios.urls')),
    
    path('api/clientes/', include('aplicaciones.clientes.urls')),      # Fase 2-3
    path('api/productos/', include('aplicaciones.productos.urls')),    # Fase 3-4
    path('api/facturacion/', include('aplicaciones.facturacion.urls')), # Fase 3-4
    path('api/inventario/', include('aplicaciones.inventario.urls')),   # Fase 5
    #path('api/contabilidad/', include('aplicaciones.contabilidad.urls')), # Fase 6
    #path('api/reportes/', include('aplicaciones.reportes.urls')),       # Fase 7
]

# Configuración para archivos estáticos y multimedia en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
    # Django Debug Toolbar (si está instalado)
    try:
        import debug_toolbar
        urlpatterns += [
            path('__debug__/', include(debug_toolbar.urls)),
        ]
    except ImportError:
        pass

# Configuración del panel de administración
admin.site.site_header = 'FELICITAFAC Administración'
admin.site.site_title = 'FELICITAFAC'
admin.site.index_title = 'Sistema de Facturación Electrónica'
admin.site.site_url = '/'

# Handler de errores personalizados
handler404 = 'configuracion.views.error_404'
handler500 = 'configuracion.views.error_500'
handler403 = 'configuracion.views.error_403'
handler400 = 'configuracion.views.error_400'