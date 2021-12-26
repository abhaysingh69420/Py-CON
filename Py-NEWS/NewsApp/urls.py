from django.urls import path
from .views import index,TechRadar, techcrunch, wired ,theverge, thenextweb, engadget 

urlpatterns = [
path('', index, name = 'index'),
path('TechRadar/', TechRadar, name = 'TechRadar'),
path('techcrunch/', techcrunch, name = 'techcrunch'),
path('wired/', wired, name = 'wired'),
path('theverge/', theverge, name = 'theverge'),
path('thenextweb/', thenextweb, name = 'thenextweb'),
path('engadget/', engadget, name = 'engadget'),

]
