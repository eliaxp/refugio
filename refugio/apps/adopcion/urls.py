from django.conf.urls import url
from apps.adopcion.views import inicio, SolicitudList

# para poder usarla ahi que importarla.

urlpatterns = [
    url(r'^$', inicio, name='inicio'),
    url(r'^solicitud/listar$', SolicitudList.as_view(), name='solicitud_listar'),

]
