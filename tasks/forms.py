from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'add new task'}))
    priority = forms.Select()
    
    class Meta:
        model = Task
        fields = 'title' , 'user', 'priority'