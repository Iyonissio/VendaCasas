from django.urls import path
from .views import ListasView, ListaView,SearchView

urlpatterns = [
    path('', ListasView.as_view()),
    path('search', SearchView.as_view()),
    path('<slug>', ListaView.as_view()),
]