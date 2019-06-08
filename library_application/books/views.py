from django.shortcuts import render

from django import forms
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Books, BooksInformation
from .forms import SearchForm

class BooksListView(ListView):
    model = Books
    queryset = Books.objects.all()
    template_name = 'books/books_list.html'


class BooksInformationView(DetailView):
    model = Books
    template_name = 'information/information_detail.html'
    context_object_name = 'book'


class CreateBooksView(CreateView):
    model = Books
    fields = ['name', 'is_available']
    template_name = 'books/books_create.html'
    success_url = reverse_lazy('books_list')

    def form_valid(self, form):
        return super().form_valid(form)


class CreateBooksInformationView(CreateView):
    model = BooksInformation
    fields = ['about_book', 'author', 'edition', 'isbn_number']
    template_name = 'information/information_create.html'
    success_url = reverse_lazy('books_list')

    def form_valid(self, form):
        form.instance.book_id = self.kwargs.get('pk')
        return super(CreateBooksInformationView, self).form_valid(form)


class EditInformationView(UpdateView):
    model = BooksInformation
    fields = ['about_book', 'author', 'edition', 'isbn_number']
    template_name = 'information/information_edit.html'
    success_url = reverse_lazy('books_list')
    context_object_name = 'info'
    


class DeleteBooksView(DeleteView):
    model = Books
    template_name = 'books/books_delete.html'
    success_url = reverse_lazy('books_list')
    context_object_name = 'books'


class InformationSearchView(FormView):
    template_name = 'information/information_search.html'
    form_class = SearchForm
    model = BooksInformation

 
    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        if form.is_valid():
            query = form.cleaned_data['search']
            print(query)
            queryset = BooksInformation.objects.filter(about_book__contains=query).all()    
            return render(
                request, self.template_name, {
                    'form': form, 'names': queryset,
                })

        return render(request, self.template_name, {'form': form})

