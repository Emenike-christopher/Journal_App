from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import journal
from .form import journalCreationForm
from django.urls import reverse_lazy

class journalView(ListView):
    model = journal
    template_name = 'journal/home.html'
    context_object_name = 'journals'


class journalDetailView(DetailView):
    model = journal
    template_name = 'journal/detail.html'

class journalCreateView(CreateView):
    model = journal
    template_name = 'journal/create.html'
    form_class = journalCreationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class journalUpdateView(UpdateView):
    model = journal
    form_class = journalCreationForm
    template_name = 'journal/update.html'
    success_url = reverse_lazy('home')

class journalDeleteView(DeleteView):
    model = journal
    template_name = 'journal/delete.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)