from django.shortcuts import render
from django.views.generic import TemplateView
from album.models import Album

class HomePageView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albums'] = Album.objects.all()  # Retrieve all objects from MyModel
        return context