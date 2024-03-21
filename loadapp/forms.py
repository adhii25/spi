from django import forms
from loadapp.models import Categories, Movies


class CategoryForm(forms.ModelForm):


    class Meta:
        model=Categories
        fields=['category']

class MoviesForm(forms.ModelForm):
    class Meta:
        model=Movies
        fields=['movie','poster','release_date','description','actors','category']