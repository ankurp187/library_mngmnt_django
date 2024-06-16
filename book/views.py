from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404,render,redirect

from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Book, Assignment

from .forms import AssignmentForm

# Create your views here.

class BookDetailView(generic.ListView):
    template_name = 'book/book_details.html'
    context_object_name = 'books'

    def get_queryset(self) -> QuerySet[Any]:
        return Book.objects.order_by("-publish_date")


def assignBook(request):
    return render(request,"book/book_assign.html")

def assignBookDef(request):
    roll = request.POST.get('roll_id')
    book_i = request.POST.get('book_id')
    book = get_object_or_404(Book,pk=book_i)
    
    Assignment(roll_id = roll ,book_id = book).save()
    book.quantity = book.quantity-1
    book.save()

    return HttpResponseRedirect(reverse("book:assign_book"))


