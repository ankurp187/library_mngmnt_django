from django.urls import path

from . import views

# Added to differentiate between different apps inside the same project
app_name = "book"

urlpatterns = [
    path("book_details/", views.BookDetailView.as_view(), name="book_details"),
    path("assign_book/", views.assignBook, name="assign_book"),
    path("assign_book_def/", views.assignBookDef, name="assign_book_def"),
    # path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # path("<int:question_id>/vote/", views.vote, name="vote"),
]




