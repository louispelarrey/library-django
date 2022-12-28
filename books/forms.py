from django import forms

Category = (
    ('1', 'Roman'),
    ('2', 'Science Fiction'),
    ('3', 'Thriller'),
    ('4', 'Horror'),
)
Author = (
    ('1', 'Stephen King'),
    ('2', 'J.K. Rowling'),
    ('3', 'J.R.R. Tolkien'),
    ('4', 'George R.R. Martin'),
)
Editor = (
    ('1', 'Hachette Livre'),
    ('2', 'HarperCollins'),
    ('3', 'Penguin Random House'),
    ('4', 'Simon & Schuster'),
)
Collection = (
    ('1', 'Harry Potter'),
    ('2', 'Le Seigneur des Anneaux'),
    ('3', 'Game of Thrones'),
    ('4', 'Les Chroniques de Narnia'),
)
class AddBookForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea , required=True)
    category = forms.ChoiceField(choices=Category)
    author = forms.ChoiceField(choices=Author)
    editor = forms.ChoiceField(choices=Editor)
    collection = forms.ChoiceField(choices=Collection)
