from django import forms
from django.forms import ModelForm
from jobopening.models import Book,Author


class AuthorForm(ModelForm):
    class Meta:
        model = Author

BookFormset = inlineformset_factory(Author, Book,
    fields=('book_name', 'publisher_name'), extra=1,
    can_delete=False)