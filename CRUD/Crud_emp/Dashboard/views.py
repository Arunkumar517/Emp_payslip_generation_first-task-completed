from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404, redirect
from django.template.loader import get_template
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.timezone import now
from weasyprint import HTML
from django.core.paginator import Paginator
from .forms import EmployeeForm
from .models import Employee
from Dashboard.models import Employee

from .views import *

#Dashboard.
def Interface(request):
    employees = Employee.objects.all()
    return render(request, 'Dashboard/Interface.html',{'employees': employees})


#Create page.
def create_employee(request):
    if request.method =="POST":
        form=EmployeeForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('/')
    else:
        form = EmployeeForm()

    return render(request,'Dashboard/Createpage.html',{'form':form})

#View page.
def View_employee(request, id):
    employee = get_object_or_404(Employee, id=id)  # Get employee by ID
    return render(request, 'Dashboard/viewpage.html', {'employee': employee})
#Edit page.
def Edit_employee(request, pk):
    employee = get_object_or_404(Employee,pk=pk)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect(reverse('interface', kwargs={'employee_id': employee.id}))
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'Dashboard/Editpage.html', {'employee': employee})
        
#delete view
def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        employee.delete()
    return redirect('Interface')

#Pdf_generation.
def generate_pdf(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    html_string = render_to_string('Dashboard/Viewpage.html', {'employee': employee,})
    pdf = HTML(string=html_string).write_pdf()
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="payslip_{employee_id}.pdf"'
    return response




