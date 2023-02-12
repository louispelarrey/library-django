from django import forms
from .models import Book, Author, Collection, Editor, Category

class AddCategoryForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)

class AddAuthorForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)

class AddEditorForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)

class AddCollectionForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)

class AddBookForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea , required=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    editor = forms.ModelChoiceField(queryset=Editor.objects.all())
    collection = forms.ModelChoiceField(queryset=Collection.objects.all())
    cover = forms.ImageField(required=False)

    class Meta:
        model = Book
        fields = ['title', 'description', 'category', 'author', 'editor', 'collection', 'cover']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'editor': forms.Select(attrs={'class': 'form-control'}),
            'collection': forms.Select(attrs={'class': 'form-control'}),
            'cover': forms.FileInput(attrs={'class': 'form-control'}),
        }