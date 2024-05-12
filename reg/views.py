from django.shortcuts import render, redirect
from .models import Student, Course, StudentReg
from .forms import UserRegistrationForm, CourseForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.


@login_required
def add_student(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        major = request.POST.get('major')
        avg = request.POST.get('avg')

        # Student.objects.create(name=name, major=major, avg=avg)
        student = Student()
        student.name = name
        student.major = major
        student.avg = avg
        student.user = request.user

        student.save()

    return render(request, 'student_form.html')


def user_in_group(user):
    return user.groups.filter(name='admin').exists()


@user_passes_test(user_in_group)
def add_course(request):

    if request.method == 'POST':

        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses')

    return render(request, 'course_form.html')


@login_required
def courses(request, code=None):

    reg_courses = request.session.get('reg_courses', [])

    if code:
        course_list = Course.objects.filter(code=code)
    else:
        course_list = Course.objects.exclude(code__in=reg_courses)  # SELECT * FROM courses

    return render(request, 'courses.html', {"courses": course_list, "reg_courses": reg_courses})


@login_required
def reg_course(request, code):

    user_id = request.user.id
    student = Student.objects.get(user_id=user_id)
    course = Course.objects.get(code=code)

    student_reg = StudentReg()
    student_reg.student = student
    student_reg.course = course
    student_reg.save()

    reg_courses = request.session.get('reg_courses', [])
    reg_courses.append(code)

    request.session['reg_courses'] = reg_courses

    return redirect('student_courses')


@login_required
def unreg_course(request, code):

    user_id = request.user.id
    student = Student.objects.get(user_id=user_id)
    course = Course.objects.get(code=code)

    StudentReg.objects.filter(course=course, student=student).delete()

    return redirect('student_courses')


@login_required
def student_courses(request):

    user_id = request.user.id

    student = Student.objects.get(user_id=user_id)
    student_reg_list = StudentReg.objects.filter(student=student)
    courses = []
    for reg in student_reg_list:
        courses.append(reg.course)

    return render(request, 'student_courses.html', {"courses": courses})


@login_required
def students(request, id=None):

    username = request.user.username

    if id:
        students_list = Student.objects.filter(id=id)
    else:
        students_list = Student.objects.all()  # SELECT * FROM students

    return render(request, 'students.html', {"students": students_list, 'username': username})


def delete(request, id):

    Student.objects.get(id=id).delete()
    return redirect('students')


def update(request, id):

    student = Student.objects.get(id=id)

    if request.method == 'POST':
        name = request.POST.get('name')
        major = request.POST.get('major')
        avg = request.POST.get('avg')

        student.name = name
        student.major = major
        student.avg = avg
        student.save()

    return render(request, 'student_form.html', {"student": student})


def register(request):
    error = ""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
        else:
            error = "Invalid data"

    form = UserRegistrationForm()

    return render(request, 'registration.html', {"form": form, "error": error})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('students')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password!'})

    return render(request, 'login.html')


def user_logout(request):

    if request.user:
        logout(request)
    return redirect('login')









