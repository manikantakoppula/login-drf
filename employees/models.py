from django.db import models



class employee(models.Model):
    employee_name = models.CharField(max_length=200)
    employee_salary = models.IntegerField()
    employee_address = models.TextField(max_length=200)
    employee_created = models.TimeField(auto_created=True)

    def __str__(self):
        return self.employee_name