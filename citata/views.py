from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Quote

#
# def quote_list(request):
#     quotes = Quote.objects.all()
#     return render(request, 'quote_list.html', {'quotes': quotes})
# # Create your views here.

class QuoteList(ListView):
    model = Quote


class QuoteDetailView(DetailView):
    model = Quote

class QuoteCreate(CreateView):
    model = Quote
    fields = ['title', 'authors',]
    success_url = reverse_lazy('quote_list')

class QuoteUpdate(UpdateView):
    model = Quote
    fields = ['title', 'authors',]
    success_url = reverse_lazy('quote_list')

class QuoteDelete(DeleteView):
    model = Quote
    success_url = reverse_lazy('quote_list')