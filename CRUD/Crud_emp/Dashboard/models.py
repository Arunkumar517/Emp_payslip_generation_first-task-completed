from django.db import models

class Employee(models.Model):
    Employee_name = models.CharField(max_length=100)
    Employee_id = models.IntegerField(unique=True)
    Department = models.CharField(max_length=200)
    Designation = models.CharField(max_length=100)
    Basic_pay = models.DecimalField(max_digits=10, decimal_places=2)
    employee_pf = models.DecimalField(max_digits=10, decimal_places=2)
    Allowance = models.DecimalField(max_digits=10, decimal_places=2)
    Deductions = models.DecimalField(max_digits=10, decimal_places=2)
    Net_salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.Employee_name
