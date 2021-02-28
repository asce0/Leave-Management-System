from django.db import models
import datetime

class EmployeeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


    def all_employees(self):
        '''
        Employee.objects.all_employee() -> returns all employees
        '''
        return super().get_queryset()







    


