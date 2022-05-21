from django import forms 
from .models import Review
from django.forms import ModelForm

# class ReviewForm(forms.Form):

#     first_name = forms.CharField(label='First Name', max_length=100)
#     email = forms.EmailField(label='Email')
#     review = forms.CharField(label='Please write the review', widget=forms.Textarea())

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__"