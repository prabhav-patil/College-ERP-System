from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.db.models import Q
from django.http import HttpRequest
#import mysite.myhash as myhash
from django.views.decorators.csrf import csrf_exempt
from erp.models import student
from erp.models import faculty
from erp.models import department
from erp.models import enrollment
from erp.models import prereq
from erp.models import course
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.contrib.auth.hashers import make_password

# Create your views here.
'''
What all views do we need?
-> Students' enrolled courses ( enrolled )
-> The courses that the student can enroll in ( depending on the pre-requisite ) ( can enroll )
-> Teachers' currently taking courses ( faculty courses )
-> Students' enrolled in each course taken by the given faculty ( enrollment view )
'''
'''  
def enrolled(request, roll_num):
    enrolled = enrollment.objects.filter(roll_number = roll_num)
    courses = []
    for enr in enrolled:
        courses.append(enr.course_id)
    name = []
    for crs in courses:
        name.append(crs)

    return HttpResponse(name)


def can_enroll(request, roll_num):
    enrolled = enrollment.objects.filter(roll_number = roll_num)
    prereq_set = set()
    for enr in enrolled:
        prereq_set.add(enr.course_id)
        
    output = []
    
    courses = prereq.objects.all()
    for crs in courses:
        required = prereq.objects.filter(c_id = crs.c_id)
        flag = 0
        for rq in required:
            if(rq.p_id not in prereq_set):
                flag = 1
                break
        if(flag==0):
            output.append(crs.c_id)
    
    return HttpResponse(len(output))
'''

def home(request):
    return render(request, "home.html")
  
def faculty_course(request, faculty_id):
    courses = course.objects.filter(faculty_id=faculty_id)
    context = {
        'courses': courses,
        'faculty_id': faculty_id
    }
    return render(request, 'faculty_courses.html', context)
    
def enrollmentview(request, course_id):
        enrollments = enrollment.objects.filter(course_id=course_id)
        students = []
        for enroll in enrollments:
            stud = student.objects.get(roll_number=enroll.roll_number)
            students.append({
                'name': stud.name,
                'roll_number': stud.roll_number,
                'enrollment_date': enroll.enrollment_date,
                'grade': enroll.grade,
            })
        context = {
            'students': students,
            'course_id': course_id
        }
        return render(request, 'course_enrollment.html', context)
 
''' 
def can_enroll(request, roll_number):
        completed_courses = enrollment.objects.filter(roll_number=roll_number).values_list('course_id', flat=True)
        courses = course.objects.filter((prereq.p_id in completed_courses)).exclude(enrollment__roll_number=roll_number)
        context = {
            'courses': courses,
            'roll_number': roll_number
        }
        return render(request, 'student_courses.html', context)
'''
        
        
def student_enrollable_courses(request, roll_number):
    # Get all courses from the Course table
    all_courses = course.objects.all()

    # Get courses the student has already enrolled in
    enrolled_courses = enrollment.objects.filter(roll_number=roll_number).values_list('course_id', flat=True)

    # Get courses that have prerequisites and filter them based on the student's previous enrollments
    courses_with_prereqs = prereq.objects.filter().values_list('c_id', flat=True)
    eligible_courses = course.objects.exclude(course_id__in=enrolled_courses).exclude(course_id__in=courses_with_prereqs)

    context = {'roll_number': roll_number, 'courses': eligible_courses}

    return render(request, 'student_courses.html', context)
    
def faculty_by_department(request, department_id):
    # Get all faculty members for the given department
    faculty_members = faculty.objects.filter(department_id=department_id)

    context = {'department_id': department_id, 'faculty_members': faculty_members}

    return render(request, 'faculty_list.html', context)
    
def department_names(request):
    # Get all department names from the Department table
    departments = department.objects.all()

    context = {'departments': departments}

    return render(request, 'department_list.html', context)
    
def enrolled_courses(request, roll_number):
    enrollments = enrollment.objects.filter(roll_number=roll_number)
    return render(request, 'enrolled_courses.html', {'enrollments': enrollments})
    
#def student_login(request):
#    return render(request, 'student_login.html')


'''
def student_login(request):
    if request.method == 'POST':
        roll_number = request.POST['roll_number']
        password = request.POST['password']

        try:
            stud = student.objects.get(roll_number=roll_number)
        except student.DoesNotExist:
            error_message = "Invalid roll number or password"
            return render(request, 'student_login.html', {'error_message': error_message})

        if check_password(password, stud.password):
            request.session['student_roll_number'] = roll_number
            return redirect('dashboard')
        else:
            error_message = "Invalid roll number or password"
            return render(request, 'student_login.html', {'error_message': error_message})
    else:
        return render(request, 'student_login.html')
'''
def student_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = student.objects.filter(roll_number=username, password=password).first()

        if user is not None:
            # Redirect to dashboard page with student_id as a parameter
            return redirect('student_dashboard', student_id=user.roll_number)
        else:
            # Return an 'invalid login' error message.
            error_message = "Invalid login credentials"
            return render(request, 'student_login.html', {'error_message': error_message})
    else:
        # Display the login form
        return render(request, 'student_login.html')


def faculty_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = faculty.objects.filter(email=username, password=password).first()
        
        if user is not None:
            # Redirect to dashboard page with student_id as a parameter
            return redirect('faculty_dashboard', faculty_id=user.faculty_id)
        else:
            # Return an 'invalid login' error message.
            error_message = "Invalid login credentials"
            return render(request, 'faculty_login.html', {'error_message': error_message})
    else:
        # Display the login form
        return render(request, 'faculty_login.html')
    
def student_dashboard(request, student_id):
    # Retrieve the student from the database
    studen = student.objects.get(roll_number=student_id)

    # Render the dashboard template with the student data
    context = {
        'student': studen,
    }
    return render(request, 'student_dashboard.html', context)

def faculty_dashboard(request, faculty_id):
    # Retrieve the student from the database
    facult = faculty.objects.get(faculty_id=faculty_id)

    # Render the dashboard template with the student data
    context = {
        'faculty': facult,
    }
    return render(request, 'faculty_dashboard.html', context)
 
''' 
def student_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            roll_number = form.cleaned_data.get('roll_number')
            password = form.cleaned_data.get('password')
            student = authenticate(request, roll_number=roll_number, password=password)
            if student is not None:
                login(request, student)
                return redirect('student_dashboard')
            else:
                form.add_error(None, "Invalid roll number or password.")
    else:
        form = LoginForm()
    return render(request, 'student_login.html', {'form': form})
'''
    
def student_logout(request):
    logout(request)
    return redirect('student_login')
    
def faculty_logout(request):
    logout(request)
    return redirect('faculty_login')
    
'''
def student_dashboard(request):
    if not request.user.is_authenticated or not isinstance(request.user, Student):
        return redirect('student_login')
    return render(request, 'student_dashboard.html', {'student': request.user})
'''

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('student_dashboard')
        else:
            # Handle invalid login
            return render(request, 'student_login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'student_login.html')