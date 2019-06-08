
from django.urls import path
from .views import (
    BooksListView,
    CreateBooksView,
    CreateBooksInformationView,
    EditInformationView,
    DeleteBooksView,
    BooksInformationView,
    InformationSearchView,
    )

urlpatterns = [
    path('',  BooksListView.as_view(), name = 'books_list'),
    path('createbooks/', CreateBooksView.as_view(), name = 'books_create'),
    path('<int:pk>/createinfo',  CreateBooksInformationView.as_view(), name = 'information_create'),
    path('<int:pk>/editinfo',  EditInformationView.as_view(), name = 'information_edit'),
    path('<int:pk>/deletebooks', DeleteBooksView.as_view(), name = 'books_delete'),
    path('<int:pk>', BooksInformationView.as_view(), name = 'information_detail'),
    path('search/', InformationSearchView.as_view(), name = 'information_search' )
]
