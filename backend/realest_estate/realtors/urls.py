from django.urls import path
from .views import Corretor_de_ImoveisListView,Corretor_de_ImoveisView,MaisVendidosView

urlpatterns = [
    path('', Corretor_de_ImoveisListView.as_view()),
    path('maisvendido', MaisVendidosView.as_view()),
    path('<pk>', Corretor_de_ImoveisView.as_view()),
]