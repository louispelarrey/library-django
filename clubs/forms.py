from django import forms
from .models import Club, Session
from books.models import Book
from libraries.models import Library
from bootstrap_datepicker_plus.widgets import DatePickerInput

class AddClubForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea , required=True)
    capacity = forms.IntegerField(required=True)
    book = forms.ModelChoiceField(queryset=Book.objects.all())

    class Meta:
        model = Club
        fields = ['name', 'description', 'capacity', 'book']

class AddSessionForm(forms.Form):
    date = forms.DateField(widget=DatePickerInput(), required=True)