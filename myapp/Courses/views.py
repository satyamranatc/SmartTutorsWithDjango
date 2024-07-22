from django.shortcuts import render
from .models import CourseData
# Create your views here.
def Courses(request):
    AllCourses = CourseData.objects.all()
    return render(request, 'Courses.html',{"AllCourses":AllCourses})