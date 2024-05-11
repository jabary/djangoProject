from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Student, Course, StudentReg
from .forms import UserRegistrationForm, CourseForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


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


def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses')  # Redirect to login page after successful registration
    else:
        form = CourseForm()

    return render(request, 'course_form.html', {'form': form})



@login_required
def courses(request, code=None):

    if code:
        courses_list = Course.objects.filter(code=code)
    else:
        courses_list = Course.objects.all()  # SELECT * FROM students

    return render(request, 'courses.html', {"courses": courses_list})


@login_required
def reg_course(request, code):

    user_id = request.user.id
    student = Student.objects.get(user_id=user_id)
    course = Course.objects.get(code=code)
    student_reg = StudentReg()
    student_reg.student = student
    student_reg.course = course
    student_reg.save()

    return redirect('student_courses')


@login_required
def unreg_course(request, code):

    course = Course.objects.get(code=code)

    StudentReg.objects.filter(course=course).delete()

    return redirect('student_courses')


@login_required
def student_courses(request):

    user_id = request.user.id
    student = Student.objects.get(user_id=user_id)

    student_reg = StudentReg.objects.filter(student=student)

    courses = [reg.course for reg in student_reg]

    return render(request, 'student_courses.html', {"courses": courses})


def user_in_group(user):
    return user.groups.filter(name='admin').exists()


@user_passes_test(user_in_group)
def students(request, id=None):

    user = request.user

    if id:
        students_list = Student.objects.filter(id=id)
    else:
        students_list = Student.objects.all()  # SELECT * FROM students

    return render(request, 'students.html', {"students": students_list, "username": user.username})


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
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'registration.html', {'form': form})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('students')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password!'})

    return render(request, 'login.html')


def user_logout(request):
    if request.user:
        logout(request)

        return redirect('login')


















