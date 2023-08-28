from django import forms

from .models import Task


class TaskForm(forms.Form):
    title = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'add new task'}))
    priority = forms.ChoiceField()
    
    class Meta:
        model = Task
        fields = 'title' , 'user' , 'priority'