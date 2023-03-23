
from django.urls import path
from .views import EmployeeViewSet


urlpatterns = [
    path('', EmployeeViewSet.as_view())
]
