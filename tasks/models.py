from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    
    HIGH_PRIORITY = 'H'
    LOW_PRIORITY = 'L'
    MIDDLE_PRIORITY = 'M'
    
    priority_choices = (
        (HIGH_PRIORITY , 'High Priority'),
        (LOW_PRIORITY , 'Low Priority'),
        (MIDDLE_PRIORITY , 'Middle Priority'),
    )
    user = models.ForeignKey(User , on_delete=models.CASCADE , null=True , blank=True)
    title = models.CharField(max_length=200)
    priority = models.CharField(max_length=1 , choices=priority_choices , default=HIGH_PRIORITY)
    complete = models.BooleanField(default=False)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        order_with_respect_to = 'user'