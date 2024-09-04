from django.http import JsonResponse
from .models import Note


def get_all_notes(request):
    notes = Note.objects.all()
    notes_list = list(notes.values())
    return JsonResponse(notes_list, safe=False)
