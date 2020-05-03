from django.urls import path
from hamburguesa import views

urlpatterns = [
    path('hamburguesa/', views.HamburguesaView.as_view()),
    path('hamburguesa/<hamburguesa_id>', views.HamburguesaIdView.as_view()),
    path('hamburguesa/<hamburguesa_id>/ingrediente/<ingrediente_id>', views.IngredienteEnHamburguesaView.as_view()),
    path('ingrediente/', views.IngredienteView.as_view()),
    path('ingrediente/<ingrediente_id>', views.IngredienteIdView.as_view()),
]