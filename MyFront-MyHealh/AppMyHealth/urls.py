from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pageDeRFID/', views.pageDeRFID, name='pageDeRFID'),
    path('pageDeBiométrique/', views.pageDeBiométrique, name='pageDeBiométrique'),
    path('accueil/', views.accueil, name='accueil'),
    path('hospitalisation/', views.hospitalisation, name='hospitalisation'),
    path('attente/', views.attente, name='attente'),
    path('consultation/', views.consultation, name='consultation'),
    path('consBio/', views.consBio, name='consBio'),
    path('accueilPat/', views.accueilPat, name='accueilPat'),
    path('Ordonnace/', views.Ordonnace, name='Ordonnace'),
    path('impression/', views.impression, name='impression'),

]
