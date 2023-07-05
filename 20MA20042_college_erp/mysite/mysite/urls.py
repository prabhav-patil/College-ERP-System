"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from erp import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('erp/faculty/<int:faculty_id>/courses/', views.faculty_course, name='faculty_course'),
    path('erp/student/<str:roll_number>/available/', views.student_enrollable_courses, name='student_enrollable_courses'),
    path('erp/course/<int:course_id>/enrollment/', views.enrollmentview, name='enrollmentview'),
    path('erp/department/<int:department_id>/faculty/', views.faculty_by_department, name='faculty_by_department'),
    path('erp/department/names/', views.department_names, name='department_names'),
    path('erp/student/<str:roll_number>/enrolled/', views.enrolled_courses, name='enrolled_courses'),
    path('erp/faculty/login/', views.faculty_login, name='faculty_login'),
    path('erp/student/login/', views.student_login, name='student_login'),
    path('login/', views.login_view, name='login'),
    path('student/logout/', views.student_logout, name='student_logout'),
    path('faculty/logout/', views.faculty_logout, name='faculty_logout'),
    path('student/<str:student_id>/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('faculty/<int:faculty_id>/dashboard/', views.faculty_dashboard, name='faculty_dashboard'),
    path('', views.home, name='home'),
]
