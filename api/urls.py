from django.urls import path

from .views import get_all_notes


urlpatterns = [
    path('notes/', get_all_notes, name='get_all_notes')
]
