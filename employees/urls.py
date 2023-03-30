
from django.urls import path
from .views import *


urlpatterns = [
    path('', EmployeeList.as_view()),
    path('<id>/', EmployeeById.as_view()),
]
