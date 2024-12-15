from django.urls import path
from . import views

urlpatterns = [
    path('cv/', views.cv_view, name='cv'),
    path('stages/', views.stages_view, name='stages'),
    path('travaux/', views.travaux_view, name='travaux'),
    path('certifications/', views.certifications_view, name='certifications'),
]
