from django.http import HttpResponse
import datetime
from django.shortcuts import render

def home(request):
    isActive=True
    if request.method=='POST':
        check=request.POST.get('check')
        print(check)
        if check is None:isActive=False
    date=datetime.datetime.now()
    
    name="Durga Prakash"
    list_of_programs=[
        'a','b','c','d'
    ]
    student={
        'student_name':"Durga",
        'student_college':"kucet",
        'student_city':'Peddapalli'
    }
    data={
        'date':date,
        'isActive':isActive,
        'name':name,
        'list_of_programs':list_of_programs,
        'student_data':student
    }
    return render(request,"home.html",data)

def about (request):
    # return HttpResponse("<h1>This is About page</h1>")
    return render(request,"about.html",{})

def services(request):
    # return HttpResponse("<h1>This is Service Page</h1>")
    return render(request,"service.html",{})