# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Book, Author, BookInstance, Genre
from django.shortcuts import render
from django.views import generic

# Create your views here.

def index(request):
    """
    View function for home page
    """

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact = "a").count()
    num_authors = Author.objects.count()

    return render(
        request,
        "index.html",
        context = {"num_books": num_books, "num_instances": num_instances, "num_instances_available": num_instances_available, "num_authors": num_authors},
    )

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2

    # context_object_name = "my_book_list"
    # queryset = Book.objects.filter(title__icontains = "Potter")[:5]
    # template_name = "books/my_arbitrary_template_list_name.html"

    def get_queryset(self):
        return Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context["misc data"] = "this is misc data"
        return context

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author
