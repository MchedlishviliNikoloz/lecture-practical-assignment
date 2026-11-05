from django.contrib import admin

from first_app.models import Company, Employee, Project, Department, Position, EmployeeProfile
admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Project)
admin.site.register(Department)
admin.site.register(Position)
admin.site.register(EmployeeProfile)

# Register your models here.
