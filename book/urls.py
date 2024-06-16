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
    path("allAssignments/",views.allAssignmentsView.as_view(),name="all_assign"),
    path("curr_Assignments/",views.currAssignmentsView.as_view(),name="curr_assign"),
    path("stud_Assignments/<str:stud_id>/",views.studAssignmentsView.as_view(),name="stud_assign"),
    path("assignment_error/<str:stud_id>/",views.assignmentErrorView.as_view(),name="assignment_error"),
]




