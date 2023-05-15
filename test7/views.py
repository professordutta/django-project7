from django.shortcuts import render
from .forms import EmployeeForm, UpdateForm, DeleteForm
from django.shortcuts import HttpResponse, redirect, get_object_or_404
from .models import Employee

def home(request):
    form=EmployeeForm()
    return render(request,'test7/home.html',{'form':form})

def add_record(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponse('<h2>Data Added Successfully</h2>')

def read_record(request):
    employee=Employee.objects.all()
    return render(request,'test7/read.html',{'employee':employee})

def search(request):
    query=request.GET['query']
    if len(query) > 0:
        if Employee.objects.filter(first_name__istartswith = query):
            employee=Employee.objects.filter(first_name__istartswith = query)
            return render(request,'test7/read.html',{'employee':employee})
        else:
            return HttpResponse("<h2>Search not found! Try with other keywords</h2>")
    else:
        return redirect("read_record")
    
def update_record(request):
    uform = UpdateForm()
    return render(request,'test7/update.html',{'uform':uform})

def update_info(request):
    if request.method=="POST":
        email_ID = request.POST.get('uemail')
        fname = request.POST.get('first_name')
        lname = request.POST.get("last_name")
        new_email = request.POST.get("email")
        new_phone = request.POST.get("phone")
        for x in Employee.objects.all():
            if x.email == email_ID:
                obj = Employee.objects.get(email=email_ID)
                obj.first_name = fname
                obj.last_name = lname
                obj.phone = new_phone
                for y in Employee.objects.all():
                    if (y.email == new_email):
                        return HttpResponse("<h2>This email already exists! Try another..</h2>")
                    else:
                        obj.email = new_email
                obj.save()
            return HttpResponse("<h2>Data updated</h2>")
        
def delete(request):
    dform = DeleteForm()
    return render(request,'test7/delete.html',{'dform':dform})

def delete_info(request):
    if request.method == "POST":
        demail = request.POST.get('email')

        obj = get_object_or_404(Employee, email = demail)
        obj.delete()
        return HttpResponse("<h2>Deleted</h2>")
