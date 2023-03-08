from django.shortcuts import render,redirect
from blog.models import Course
from .forms import CourseForm

# Create your views here.
def index(request):
    courses=Course.objects.all()
    return render(request, 'base.html', {'courses': courses})

def course_delete(request, id):
    course=Course.objects.get(id=id)
    course.delete()
    return redirect('home')

def course_edit(request, id):
    course_edit=Course.objects.get(id=id)
    form=CourseForm(request.POST or None, instance=course_edit)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'course_edit.html', {'form': form, 'course_edit': course_edit})
    