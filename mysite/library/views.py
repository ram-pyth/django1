from django.shortcuts import render

from .models import Book, Author, BookInstance


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact="g").count()

    num_authors = Author.objects.count()

    kontext = {
        "num_books": num_books,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available,
        "num_authors": num_authors
    }

    return render(request, "index.html", context=kontext)


def authors(request):
    autoriai = Author.objects.all()

    kontext = {
        "authors": autoriai
    }

    return render(request, "authors.html", context=kontext)
