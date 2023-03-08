from django import forms
from .models import Course


class CourseForm(forms.ModelForm):

    name= forms.CharField(widget=forms.TextInput(attrs={'class': 'input my-2'}), label="Name:")
    description= forms.CharField(widget=forms.TextInput(attrs={'class': 'input my-2'}), label="Description:")
 
    class Meta:
        model=Course
        fields=['name', 'description']