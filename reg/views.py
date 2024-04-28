from django.shortcuts import render, redirect
from .models import Student
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

        student.save()

    return render(request, 'student_form.html')


def students(request, id=None):

    if id:
        students_list = Student.objects.filter(id=id)
    else:
        students_list = Student.objects.all()  # SELECT * FROM students

    return render(request, 'students.html', {"students": students_list})


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








