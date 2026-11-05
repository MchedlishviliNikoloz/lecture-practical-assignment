from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('companies/', views.company_list, name='company_list'),
    path('companies/<int:pk>/', views.company_detail, name='company_detail'),

    path('departments/', views.department_list, name='department_list'),

    path('employees/', views.employee_list, name='employee_list'),
    path('employees/<int:pk>/', views.employee_detail, name='employee_detail'),

    path('positions/', views.position_list, name='position_list'),

    path('projects/', views.project_list, name='project_list'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
]
