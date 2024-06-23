from typing import Any

from datetime import datetime

from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404,render,redirect

from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone,dateformat
from django.views import generic

from .models import Book, Assignment

from .forms import AssignmentForm

# Create your views here.

class BookDetailView(generic.ListView):
    template_name = 'book/book_details.html'
    context_object_name = 'books'

    def get_queryset(self) -> QuerySet[Any]:
        return Book.objects.order_by("-id")


class allAssignmentsView(generic.ListView):
    template_name = 'book/all_assignments.html'
    context_object_name = 'assignments'

    def get_queryset(self) -> QuerySet[Any]:
        return Assignment.objects.order_by("-assigned_on")


class currAssignmentsView(generic.ListView):
    template_name = 'book/current_assignments.html'
    context_object_name = 'assignments'

    def get_queryset(self) -> QuerySet[Any]:
        return Assignment.objects.filter(is_active='Y').order_by("-assigned_on")


class studAssignmentsView(generic.ListView):
    template_name = 'book/student_assignments.html'
    context_object_name = 'assignments'

    def get_queryset(self) -> QuerySet[Any]:
        return Assignment.objects.filter(roll_id=self.kwargs['stud_id']).order_by("-assigned_on")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stud_id'] = self.kwargs['stud_id']
        return context


class assignmentErrorView(generic.ListView):
    template_name = 'book/assignment_error.html'
    context_object_name = 'assignments'

    def get_queryset(self) -> QuerySet[Any]:
        return Assignment.objects.filter(roll_id=self.kwargs['stud_id'],is_active='Y').order_by("-assigned_on")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stud_id'] = self.kwargs['stud_id']
        return context


# def assignBook(request):
#     return render(request,"book/book_assign.html")

class assignBook(generic.ListView):
    template_name = 'book/book_assign.html'
    context_object_name = 'books'

    def get_queryset(self) -> QuerySet[Any]:
        return Book.objects.filter(quantity__gt=0)#.order_by("-id")


def assignBookDef(request):
    roll = request.POST.get('roll_id')
    book_i = request.POST.get('book_id')
    book = get_object_or_404(Book,pk=book_i)

    assigned_books = len(Assignment.objects.filter(roll_id=roll,is_active='Y'))
    
    if assigned_books==4:
        return HttpResponseRedirect(reverse("book:assignment_error", args=(roll,)))
    
    is_book_assigned = len(Assignment.objects.filter(roll_id=roll,book_id=book_i,is_active='Y'))
    if is_book_assigned:
        return HttpResponseRedirect(reverse("book:assignment_error", args=(roll,)))
    
    Assignment(roll_id = roll ,book_id = book).save()
    book.quantity = book.quantity-1
    book.save()

    return HttpResponseRedirect(reverse("book:assign_book"))

class check_Assignments(generic.ListView):
    template_name = 'book/book_unassign.html'
    context_object_name = 'books'

    def get_queryset(self) -> QuerySet[Any]:
        return Assignment.objects.filter(roll_id=self.kwargs['stud_id']).order_by("-assigned_on")

def check_Assignments(request):
    roll = request.POST.get('roll_id')
    assignments = Assignment.objects.filter(roll_id=roll,is_active='Y').select_related('book_id')
    books = [assignment.book_id for assignment in assignments]

    print(assignments)

    print(books)

    return render(request,"book/book_unassign.html",{'books':books})


def unassignBook(request):
    return render(request,"book/book_unassign.html")


def unassignBookDef(request):
    roll = request.POST.get('roll_id')
    book_i = request.POST.get('book_id')
    book = get_object_or_404(Book,pk=book_i)
    
    assignment_det = None
    assignment = Assignment.objects.filter(roll_id = roll ,book_id = book, is_active='Y')
    if len(assignment):
        assignment_det = assignment[0]
        assignment_det.is_active = 'N'
        assignment_det.submitted_on = dateformat.format(timezone.now(),'Y-m-d H:i:s')
        assignment_det.save()

        book.quantity = book.quantity+1
        book.save()
    else:
        return HttpResponseRedirect(reverse("book:assignment_error", args=(roll,)))

    return HttpResponseRedirect(reverse("book:unassign_book"))


