from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('resume/', views.resume, name='resume'),
    path('skills/', views.skills, name='skills'),
    path('portfolio/', views.portfolio, name='portfolio'),
]