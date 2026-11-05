from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    founded_date = models.DateField()

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='departments')

    def __str__(self):
        return f"{self.name} - {self.company.name}"

class Position(models.Model):
    title = models.CharField(max_length=150)
    salary = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title

class Employee(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class EmployeeProfile(models.Model):
    phone = models.CharField(max_length=50)
    birth_date = models.DateField()
    bio = models.TextField()
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return f"profile: {self.employee}"

class Project(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='projects')
    employees = models.ManyToManyField(Employee, related_name='projects')

    def __str__(self):
        return self.name
