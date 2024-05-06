from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),

    path('books/', views.BookListView.as_view(), name='books'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),

    path('books_edit/', views.books_edit, name='books_edit'),
    path('book/create/', views.BookCreate.as_view(), name='book_create'),
    path('book/update/<int:pk>/', views.BookUpdate.as_view(), name='book_update'),
    path('book/delete/<int:pk>/', views.BookDelete.as_view(), name='book_delete'),

    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='authors-detail'),

    path('authors_edit/', views.authors_edit, name='authors_edit'),
    path('author_edit/<int:author_id>/', views.author_edit, name='author_edit'),
    path('author_add/', views.author_add, name='author_add'),
    path('author_delete/<int:author_id>/', views.author_delete, name='author_delete'),
]
