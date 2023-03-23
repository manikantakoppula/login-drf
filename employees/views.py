
from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import EmployeeSerializer
from rest_framework.response import Response

from .models import employee


class EmployeeViewSet(APIView):
    queryset = employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        emp = employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data)