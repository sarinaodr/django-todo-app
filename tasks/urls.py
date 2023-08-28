from django.urls import path

from .views import updateT , completeT , deleteT , index

urlpatterns = [
    path('' , index , name='task-list'),
    path('update/<str:pk>/' , updateT , name='update-task'),
    path('complete/<str:pk>/' , completeT , name='complete-task'),
    path('delete/<str:pk>/' , deleteT , name='delete-task'),
]
