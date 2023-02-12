from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name="books_list"),
    path('create/', views.BookCreateView.as_view(), name='book_create'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
    path('<int:pk>/update/', views.BookUpdateView.as_view(), name='book_update'),
]
