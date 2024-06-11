from django.shortcuts import render
from django.views.generic import CreateView,UpdateView
from django.urls import reverse_lazy
from . import models
from . import forms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(login_required, name='dispatch')
class AddMusician(CreateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('homepage')

    def form_valid(self,form):
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Submit'  # Retrieve all objects from MyModel
        context['type2'] = 'Add'  # Retrieve all objects from MyModel
        return context
    

# edit musician
@method_decorator(login_required, name='dispatch')
class MusicianEditView(UpdateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'add_musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Update'  # Retrieve all objects from MyModel
        context['type2'] = 'Edit'  # Retrieve all objects from MyModel
        return context