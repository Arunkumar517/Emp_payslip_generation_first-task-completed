from django.urls import path
from . import views
from .views import *
urlpatterns = [
    path('', views.Interface, name="Interface"),
    path('Create/',views.create_employee,name="Create"),
    path('Edit/<int:pk>/',views.Edit_employee, name="Edit"),
    path('View/<int:id>',views.View_employee, name="View"),
    path('delete/<int:id>/', views.delete_employee, name="Delete"),
    path('download/<int:employee_id>/', generate_pdf, name="Download"),


]
