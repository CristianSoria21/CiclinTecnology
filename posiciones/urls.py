from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='home'),
    path('login/', views.login_juez, name='login'),
    path('posiciones/', views.posiciones, name='posiciones'),

    path('equipos/agregar/', views.agregar_equipo, name='agregar_equipo'),
    path('equipos/modificar/<int:id_equipo>', views.modificar_equipo, name='modificar_equipo'),
    path('equipos/eliminar/<int:id_equipo>', views.eliminar_equipo, name='eliminar_equipo'),
    path('equipos/', views.equipos, name='equipos'),
    path('equipos/clase/', views.EquiposListView.as_view(), name='equipos_clase'),

    path('categorias/agregar/', views.agregar_categoria, name='agregar_categoria'),
    path('categorias/modificar/<int:id_categoria>', views.modificar_categoria, name='modificar_categoria'),
    path('categorias/eliminar/<int:id_categoria>', views.eliminar_categoria, name='eliminar_categoria'),
    path('categorias/', views.categorias, name='categorias'),
    path('categorias/clase/', views.CategoriaListView.as_view(), name='categorias_clase'),

    path('carreras/carreras_list/', views.CarreraListView.as_view(), name='carrera_list'),
    path('carreras/carrera_new/', views.CarreraCreateView.as_view(), name='carrera_new'),
    path('carreras/carrera_delete/<pk>/', views.CarreraDeleteView.as_view(), name='carrera_delete'),
    path('carreras/carrera_update/<pk>/', views.CarreraUpdateView.as_view(), name='carrera_update'),
    # BASADA EN FUNCIONES
    path('carreras/carreras_listF/', views.ListarCarreras, name='carrera_listF'),
    path('carreras/carrera_newF/', views.AgregarCarrera, name='carrera_newF'),
    path('carreras/carrera_deleteF/<int:id_carrera>/', views.ELiminarCarrera, name='carrera_deleteF'),
    path('carreras/carrera_updateF/<int:id_carrera>/', views.ActualizarCarrera, name='carrera_updateF'),

    path('corredores/', views.CorredorListView.as_view(), name='corredores_list'),
    path('corredores_new/', views.CorredorCreateView.as_view(), name='corredor_new'),
    path('corredores_update/<pk>', views.CorredorUpdateView.as_view(), name='corredor_update'),
    path('corredores_delete/<pk>', views.CorredorDeleteView.as_view(), name='corredor_delete'),

    path('streaming', views.StreamCam, name='streaming'),

    path('resultados/', views.ResultadosListView.as_view(), name='resultados'),
    path('resultado_new/', views.ResultadoNewView.as_view(), name='resultado_new'),
    path('carr_equi_list/', views.CarrEquiListView.as_view(), name='carr_equi_list'),
    path('asignar_resultado/', views.AsignarPosicionView.as_view(), name='asignar_resultado'),

]
