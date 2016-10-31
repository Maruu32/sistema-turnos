from django.conf.urls import url
from . import views
from views import LoginView

urlpatterns = [
    url(r'^login$', LoginView.as_view()),
    url(r'^logout$', views.logout_view) ,
    url(r'^login$', LoginView.as_view()),
    url(r'^$', views.home),
    url(r"^cambioDia/(?P<dia>\S+)$", views.cambioDia),
    url(r'^nuevoPaciente$', views.nuevoPaciente),
    url(r'^editarPaciente/(?P<pk>[0-9]+)/$', views.editarPaciente),
    url(r'^eliminiar_paciente/(?P<pk>[0-9]+)/$', views.eliminarPaciente),
    url(r'^nuevoMedico$', views.nuevoMedico),
    url(r'^editarMedico/(?P<pk>[0-9]+)/$', views.editarMedico),
    url(r'^eliminiar_medico/(?P<pk>[0-9]+)/$', views.eliminarMedico),
    url(r'^nuevoTratamiento$', views.nuevoTratamiento),
    url(r'^editarTratamiento/(?P<pk>[0-9]+)/$', views.editarTratamiento),
    url(r'^eliminiar_tratamiento/(?P<pk>[0-9]+)/$', views.eliminarTratamiento),
    url(r'^nuevoEspecialidad$', views.nuevoEspecialidad),
    url(r'^editarEspecialidad/(?P<pk>[0-9]+)/$', views.editarEspecialidad),
    url(r'^eliminiar_especialidad/(?P<pk>[0-9]+)/$', views.eliminarEspecialidad),
    url(r'^nuevoObraSocial$', views.nuevoObraSocial),
    url(r'^editarObraSocial/(?P<pk>[0-9]+)/$', views.editarObraSocial),
    url(r'^eliminiar_obraSocial/(?P<pk>[0-9]+)/$', views.eliminarObraSocial),
    url(r'^nuevoTurno$', views.nuevoTurno),
    url(r'^editarTurno/(?P<pk>[0-9]+)/$', views.editarTurno),
    url(r'^eliminarTurno/(?P<pk>[0-9]+)/$', views.eliminarTurno),
]
