from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('authors/', views.authors_funkc, name='authors_link'),
    path('authors/<int:author_id>', views.author_func, name='author_link'),
    path('books/', views.BookListView.as_view(), name='books_link'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name="book-detail")
]
