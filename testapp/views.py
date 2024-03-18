from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from testapp.form import contactusform,CustomUserForm
# Create your views here.
def home_page(request):
    return render(request,"home.html")
@login_required
def about_page(request):
    return render(request,"about.html")
@login_required()
def project_page(request):
    return render(request,"project.html")


def contactus_page(request):
    form=contactusform()
    if request.method=="POST":
        form=contactusform(request.POST)
        if form.is_valid():
            form.save()
            
    return render(request,"contactus.html")

# signup page
def register(request):
    form=CustomUserForm()
    if request.method=="POST":
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/accounts/login/")
    

    return render(request,'registration/register.html', {'form': form})

