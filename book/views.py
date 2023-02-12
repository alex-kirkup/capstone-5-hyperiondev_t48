from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Book


class BookCreateView(CreateView):
    
    model = Book
    template_name = "book_create.html"
    success_url = reverse_lazy('books_list')
    fields = [
        "title",
        "authors",
        "publisher",
        "quantity",
    ]
    def form_valid(self, form):
        messages.success(self.request, "The book was created successfully.")
        return super().form_valid(form)


class BookDeleteView(DeleteView):
    
    model = Book
    template_name = "book_delete.html"
    success_url = reverse_lazy('books_list')

    def form_valid(self, form):
        messages.success(self.request, "The book was deleted successfully.")
        return super().form_valid(form)
    

class BookDetailView(DetailView):

    model = Book
    template_name = "book_detail.html"


class BookListView(ListView):

    model = Book
    template_name = "book_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = self.get_queryset()
        return context

    def get_queryset(self):
        query = self.request.GET.get('query')
        q = Q(title__icontains=query) | Q(authors__last_name__icontains=query)
        if query:
            object_list = self.model.objects.filter(q)
        else:
            object_list = self.model.objects.all()
        return object_list


class BookUpdateView(UpdateView):
    
    model = Book
    template_name = "book_create.html"
    success_url = reverse_lazy('books_list')
    fields = [
        "title",
        "authors",
        "publisher",
        "quantity",
    ]
    def form_valid(self, form):
        messages.success(self.request, "The book was updated successfully.")
        return super().form_valid(form)