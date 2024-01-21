from bootstrap_modal_forms.generic import BSModalCreateView
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.http.response import StreamingHttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from posiciones.models import Categoria, Carrera, Equipo, Competidor, CarrEqui
from posiciones.forms import CategoriaForm, CarreraForm, EquipoForm, CompetidorForm, CarreraEquipoForm
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
import cv2


# VISTAS BASADAS EN CLASES


class ResultadosListView(ListView):
    template_name = 'resultados/resultado.html'
    model = Carrera
    context_object_name = 'resultados'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carrera'] = self.request.GET.get('carrera')
        return context


class ResultadoNewView(ListView):
    template_name = 'resultados/resultado_new.html'
    model = Equipo
    context_object_name = 'resultados'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carrera'] = self.request.GET.get('carrera')
        return context


class AsignarPosicionView(CreateView):
    form_class = CarreraEquipoForm
    template_name = 'resultados/asignar_resultado.html'
    success_url = reverse_lazy('posiciones:resultados')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['equipo'] = self.request.GET.get('equipo')
        context['carrera'] = self.request.GET.get('carrera')
        return context


class CarrEquiListView(ListView):
    template_name = 'resultados/carr_equi_list.html'
    model = CarrEqui
    context_object_name = 'resultados'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carrera'] = self.request.GET.get('carrera')
        return context


class CarreraListView(ListView):
    template_name = 'carreras/carreras_list.html'
    model = Carrera
    context_object_name = 'carreras'
    paginate_by = 5


class CarreraCreateView(CreateView):
    form_class = CarreraForm
    template_name = 'carreras/carrera_new.html'
    success_url = reverse_lazy('posiciones:carrera_list')


@method_decorator(login_required, name='dispatch')
class CarreraUpdateView(UpdateView):
    template_name = 'carreras/carrera_update.html'
    # form_class = CarreraForm
    fields = ['nombre', 'vueltas', 'ubicacion', 'fecha']
    model = Carrera
    success_url = reverse_lazy('posiciones:carrera_list')


class CarreraDeleteView(DeleteView):
    model = Carrera
    template_name = 'carreras/carrera_delete.html'
    success_url = reverse_lazy('posiciones:carrera_list')


##############################################################################

class EquiposListView(ListView):
    template_name = 'equipos_vistaclase.html'
    model = Equipo
    context_object_name = 'equipos'
    paginate_by = 5


##############################################################################
class CorredorListView(ListView):
    template_name = 'corredores/corredores_list.html'
    model = Competidor
    context_object_name = 'corredores'


class CorredorCreateView(CreateView):
    # 1. Especificar la Forma
    form_class = CompetidorForm
    # Template que responde a la vista
    template_name = 'corredores/corredores_new.html'
    # Redireccionar
    success_url = reverse_lazy('corredores_list')


class CorredorUpdateView(UpdateView):
    template_name = 'corredores/corredores_update.html'
    # form_class = ProductoForm
    fields = ['nombre']
    model = Competidor
    success_url = reverse_lazy('corredores_list')


class CorredorDeleteView(DeleteView):
    template_name = 'corredores/corredores_list.html'
    form_class = CompetidorForm
    success_url = reverse_lazy('corredores:corredores_list')


# FIN DE LAS VISTAS BASADAS EN CLASES


# Create your views here.

def principal(request):
    return render(request, 'principal.html')


@login_required
def posiciones(request):
    return render(request, 'posiciones/posicion.html')


@login_required
def resultados(request):
    return render(request, 'resultados/resultado.html')


def login_juez(request):
    return render(request, 'iniJuez.html')


# def inicio(request):
#   categorias = Categoria.objects.all()
# Diccionario con las categorias
#  data = {
#   'categorias': categorias
# }
# return render(request,
#             'carreras/carreras_list.html',
#             context=data)

@login_required
def agregar_equipo(request):
    data = {
        'form': EquipoForm()
    }

    # Agregar la informción que se envio
    if request.method == 'POST':
        # Crear el formulario con los datos enviados
        formulario = EquipoForm(data=request.POST)
        # Validar la información
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Equipo guardado'
        else:
            data['form'] = formulario
    return render(request, 'equipos/agregar.html', data)


@login_required
def modificar_equipo(request, id_equipo):
    equipo = get_object_or_404(Equipo, id_equipo=id_equipo)
    data = {
        'form': EquipoForm(instance=equipo)
    }
    # Si el usuarioya dijo que si, POST
    if request.method == 'POST':
        formulario = EquipoForm(data=request.POST, instance=equipo)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Equipo Actualizado")
            return redirect(to='equipos')
        # Si no es valido
        data['form'] = formulario
    return render(request, 'equipos/modificar.html', data)


@login_required
def eliminar_equipo(request, id_equipo):
    equipo = get_object_or_404(Equipo, id_equipo=id_equipo)
    equipo.delete()
    messages.success(request, "Equipo Eliminado")
    return redirect(to='equipos')


@login_required
def equipos(request):
    equi = Equipo.objects.all()
    data = {
        'titulos': ['ID', 'CIUDAD', 'NOMBRE', 'CANTIDAD COMP.', 'ACCIONES'],
        'equipos': equi
    }
    return render(request, 'Equipos.html', context=data)


@login_required
def categorias(request):
    cate = Categoria.objects.all()
    data = {
        'titulos': ['ID', 'NOMBRE', 'REQUISITOS', 'ACCIONES'],
        'categorias': cate
    }
    return render(request, 'categorias.html', context=data)


class Streaming:
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def StreamCam(request):
    return StreamingHttpResponse(gen(Streaming()),
                                 content_type='multipart/x-mixed-replace; boundary=frame')


@login_required
def agregar_categoria(request):
    data = {
        'form': CategoriaForm()
    }

    # Agregar la informción que se envio
    if request.method == 'POST':
        # Crear el formulario con los datos enviados
        formulario = CategoriaForm(data=request.POST)
        # Validar la información
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Categoria guardada'
        else:
            data['form'] = formulario
    return render(request, 'categoria/agregar.html', data)


@login_required
def modificar_categoria(request, id_categoria):
    cate = get_object_or_404(Categoria, id_categoria=id_categoria)
    data = {
        'form': CategoriaForm(instance=cate)
    }
    # Si el usuarioya dijo que si, POST
    if request.method == 'POST':
        formulario = CategoriaForm(data=request.POST, instance=cate)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Categoria Actualizada")
            return redirect(to='categorias')
        # Si no es valido
        data['form'] = formulario
    return render(request, 'categoria/modificar.html', data)


class CategoriaListView(ListView):
    template_name = 'categorias_vistaclase.html'
    model = Categoria
    context_object_name = 'categorias'
    paginate_by = 5


@login_required
def eliminar_categoria(request, id_categoria):
    cate = get_object_or_404(Categoria, id_categoria=id_categoria)
    cate.delete()
    messages.success(request, "Categoria Eliminada")
    return redirect(to='categorias')


@login_required
def ListarCarreras(request):
    carreras = Carrera.objects.all()
    data = {
        'carreras': carreras
    }

    return render(request, 'carreras/carreras_listF.html', context=data)


@login_required
def AgregarCarrera(request):
    data = {
        'form': CarreraForm()
    }

    if (request.method == 'POST'):
        formulario = CarreraForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "categoria guardada"
        else:
            data['form'] = formulario

    return render(request, 'carreras/carrera_newF.html', context=data)


@login_required
def ELiminarCarrera(request, id_carrera):
    carrera = get_object_or_404(Carrera, id_carrera=id_carrera)
    carrera.delete()
    return redirect(to='posiciones:carrera_listF')


@login_required
def ActualizarCarrera(request, id_carrera):
    carrera = get_object_or_404(Carrera, id_carrera=id_carrera)
    data = {
        'form': CarreraForm(instance=carrera)
    }
    if request.method == 'POST':
        formulario = CarreraForm(data=request.POST, instance=carrera)

        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "categoria guardada"
            return redirect(to='posiciones:carrera_listF')

        data['form'] = formulario

    return render(request, 'carreras/carrera_updateF.html', context=data)
