from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import UserRegistrationForm
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


@login_required
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















