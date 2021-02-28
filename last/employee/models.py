import datetime
from django.db import models
from .managers import EmployeeManager
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
# from leave.models import Leave





class Role(models.Model):

    name = models.CharField(max_length=125)
    description = models.CharField(max_length=125,null=True,blank=True)

    created = models.DateTimeField(verbose_name=_('Created'),auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('Updated'),auto_now=True)


    class Meta:
        verbose_name = _('Role')
        verbose_name_plural = _('Roles')
        ordering = ['name','created']


    def __str__(self):
        return self.name


class Department(models.Model):


    name = models.CharField(max_length=125)
    description = models.CharField(max_length=125,null=True,blank=True)

    created = models.DateTimeField(verbose_name=_('Created'),auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('Updated'),auto_now=True)


    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')
        ordering = ['name','created']
    
    def __str__(self):
        return self.name



class Employee(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=200)
    department =  models.ForeignKey(Department,verbose_name =_('Department'),on_delete=models.SET_NULL,null=True,default=None)
    role =  models.ForeignKey(Role,verbose_name =_('Role'),on_delete=models.SET_NULL,null=True,default=None)
    startdate = models.DateField(_('Employement Date'),help_text='date of employement',blank=False,null=True)
    employeeid = models.CharField(_('Employee ID Number'),max_length=10,null=True,blank=True)
    created = models.DateTimeField(verbose_name=_('Created'),auto_now_add=True,null=True)

    objects = EmployeeManager()
    
    class Meta:
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')
        ordering = ['-created']



    def __str__(self):
        return self.get_full_name

    

    @property
    def get_full_name(self):
        name = self.name
        return name




    @property
    def can_apply_leave(self):
        pass





   

    





    def save(self,*args,**kwargs):
        '''
        overriding the save method - for every instance that calls the save method 
        perform this action on its employee_id
        added : March, 03 2019 - 11:08 PM

        '''
        get_id = self.employeeid #grab employee_id number from submitted form field
        data = get_id
        self.employeeid = data #pass the new code to the employee_id as its orifinal 
        super().save(*args,**kwargs) # call the parent save method
        # print(self.employeeid)









