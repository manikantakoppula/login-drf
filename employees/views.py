
from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import EmployeeSerializer
from rest_framework.response import Response

from .models import employee


class EmployeeList(APIView):
    queryset = employee.objects.all()
    serializer_class = EmployeeSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        emp = employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class EmployeeById(APIView):
    queryset = employee.objects.all()
    serializer_class = EmployeeSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id,format=None):
        emp = employee.objects.get(pk=id)
        serializer = EmployeeSerializer(emp)
        return Response(serializer.data)

    def put(self, request, id,format=None):
        emp = employee.objects.get(pk=id)
        serializer = EmployeeSerializer(emp,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error)
    
    def delete(self,request,id,format=None):
        emp = employee.objects.get(pk=id)
        emp.delete()
        return Response("deleted")    