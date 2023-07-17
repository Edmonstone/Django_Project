from django.shortcuts import render
from django.views.generic import ListView , DeleteView
from .models import Notes

# Create your views here.
class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name="notes/notes_list.html"

class NotesDetailView(DeleteView):
    model = Notes
    context_object_name = "note"
    template_name="notes/notes_detail.html"

