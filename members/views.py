from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from .forms import StudentForm
from .models import Student


def members(request):
    students = Student.objects.all()
    return render(request, 'first.html', {'students': students})

# Create your views here.


def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('success')
        else:
            return HttpResponse('invalid values')

    else:
        form = StudentForm()

    return render(request, 'studentForm.html', {'form': form})


def form(request):

    if request.method == "POST":
        data = request.POST
        name = request.POST.get('name')
        major = request.POST.get('major')
        avg = request.POST.get('avg')

        Student.objects.create(name=name, major=major, avg=avg)

        return render(request, 'form.html', {'data': data})

    return render(request, 'form.html')


def students(request):

    stds = Student.objects.all()[:2]  # SELECT * FROM students
    stds = Student.objects.filter(avg__lte = 80, major = 'CS')  # SELECT * FROM students WHERE major = 'CS'
    # stds = Student.objects.get(id=1)

    return render(request, 'students.html', {'students': stds})





