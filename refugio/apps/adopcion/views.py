from django.shortcuts import render
from django.views.generic import ListView, CreateView
from apps.adopcion.models import Solicitud, Persona
from apps.adopcion.forms import SolicitudForm, PersonaForm
from django.core.urlresolvers import reverse_lazy



from django.http import HttpResponse


def inicio(request):
    return render(request, 'adopcion/inicio.html')


class SolicitudList(ListView):
    model = Solicitud
    template_name = 'adopcion/solicitud_list.html'


class SolicitudCreate(CreateView):
    model = Solicitud
    template_name = 'adopcion/solicitud_form.html'
    form_class = SolicitudForm
    second_form_class = PersonaForm
    succes_url = reverse_lazy('adopcion:solicitud_listar')

    def get_context_data(self, **kwargs):
        context = super(SolicitudCreate, self).get_context_data()
