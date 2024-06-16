from django.urls import path

from . import views

# Added to differentiate between different apps inside the same project
app_name = "book"

urlpatterns = [
    path("book_details/", views.BookDetailView.as_view(), name="book_details"),
    path("assign_book/", views.assignBook, name="assign_book"),
    path("assign_book_def/", views.assignBookDef, name="assign_book_def"),
    path("unassign_book/", views.unassignBook, name="unassign_book"),
    path("unassign_book_def/", views.unassignBookDef, name="unassign_book_def"),
]



