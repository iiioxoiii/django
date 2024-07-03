from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("escola/<int:escola_id>/", views.detall, name="detall"),
    path('escola/<int:escola_id>/estudis/<int:any_oferta>/', views.estudis_per_any, name='estudis_per_any')

]
