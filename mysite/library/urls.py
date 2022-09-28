from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("authors/", views.authors_funkc, name="authors_link"),
    path("authors/<int:author_id>", views.author_func, name="author_link"),
    path("books/", views.BookListView.as_view(), name="books_link"),
    path("books/<int:pk>", views.BookDetailView.as_view(), name="book-detail"),
    path("search/", views.search, name="search_link"),
    path("mybooks/", views.LoanedBooksByUserListView.as_view(), name="my-borrowed"),
    path("register/", views.register, name="register"),
]
