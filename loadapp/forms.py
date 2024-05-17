import django.forms.widgets
from django import forms
from django.contrib.auth.models import User

from loadapp.models import Categories, Movies

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Categories
        fields=['category']

class MoviesForm(forms.ModelForm):
    class Meta:
        model=Movies
        fields=['movie','poster','release_date','description','actors','category']
        #
        widgets = {
          'release_date': forms.SelectDateWidget(empty_label=('choose year','choose month','choose day'),)
        }
        #     'movie' : forms.CharField(attrs={'class': 'form-control'}),
        #     'release_date': forms.DateField(attrs={'class': 'form-control'}),
        #     'description': forms.Textarea(attrs={'class': 'form-control'}),
        #     'actor': forms.Textarea(attrs={'class': 'form-control'}),
        #     'category': forms.Textarea(attrs={'class': 'form-control'}),
        #
        # }

    # class EditProfileForm(forms.ModelForm):
    #     class Meta:
    #         model = User
    #         fields = ['username', 'first_name', 'last_name', 'email']

    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.fields['release_date'].widget.attrs.update({'class':'form-control'})
    #     self.fields['movie'].widget.attrs.update({'class':'form-control'})
    #     self.fields['description'].widget.attrs.update({'class':'form-control'})


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
