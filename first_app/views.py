from django.shortcuts import render, get_object_or_404
from .models import Company, Department, Employee, Position, Project


def home(request):
    context = {
        'companies_count': Company.objects.count(),
        'departments_count': Department.objects.count(),
        'employees_count': Employee.objects.count(),
        'positions_count': Position.objects.count(),
        'projects_count': Project.objects.count(),
    }

    return render(request, 'home.html', context)


# Companies

def company_list(request):
    companies = Company.objects.all()

    return render(request, 'company_list.html', {
        'companies': companies
    })


def company_detail(request, pk):
    company = get_object_or_404(Company, pk=pk)

    return render(request, 'company_detail.html', {
        'company': company
    })


# Departments

def department_list(request):
    departments = Department.objects.select_related('company').all()

    return render(request, 'department_list.html', {
        'departments': departments
    })


# Employees

def employee_list(request):
    employees = Employee.objects.select_related(
        'department', 'position'
    ).all()

    return render(request, 'employee_list.html', {
        'employees': employees
    })


def employee_detail(request, pk):
    employee = get_object_or_404(
        Employee.objects.select_related('department', 'position'),
        pk=pk
    )

    return render(request, 'employee_detail.html', {
        'employee': employee
    })


# Positions

def position_list(request):
    positions = Position.objects.all()

    return render(request, 'position_list.html', {
        'positions': positions
    })


# Projects

def project_list(request):
    projects = Project.objects.prefetch_related('employees').select_related('company')

    return render(request, 'project_list.html', {
        'projects': projects
    })


def project_detail(request, pk):
    project = get_object_or_404(
        Project.objects.select_related('company').prefetch_related('employees'),
        pk=pk
    )

    return render(request, 'project_detail.html', {
        'project': project
    })