from django.shortcuts import render, redirect

# Create your views here.
from first_app import forms
from .models import Student


def Index(request):
    student_list = Student.objects.order_by("first_name")
    context = {
        'Title': "Index",
        'student_list': student_list,
    }
    return render(request, 'index.html', context=context)


def Student_Form(request):
    form = forms.StudentForm()
    if request.method == "POST":
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("first_app:index")
    context = {
        'Title': "Student Form",
        "student_form": form,
    }
    return render(request, 'student_form.html', context=context)


def StudentInfo(request, student_id):
    student_info = Student.objects.get(pk=student_id)
    context = {
        'Title': "Student Info",
        'student_info': student_info,
    }
    return render(request, 'student_info.html', context=context)


def StudentUpdate(request, student_id):
    student_info = Student.objects.get(pk=student_id)
    form = forms.StudentForm(instance=student_info)
    if request.method == "POST":
        form = forms.StudentForm(request.POST, instance=student_info)

        if form.is_valid():
            form.save(commit=True)
            return redirect("first_app:index")
    context = {
        'Title': "Student Update",
        'student_form': form,
    }
    return render(request, 'student_update.html', context=context)


def StudentDelete(request, student_id):
    student = Student.objects.get(pk=student_id).delete()
    context = {
        'delete_message': "Delete Done",
    }
    return render(request, 'student_delete.html', context=context)
