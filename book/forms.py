
from django.forms import ModelForm
from .models import Assignment


class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = ['roll_id','book_id']
