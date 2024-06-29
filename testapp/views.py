from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from testapp.form import contactusform,CustomUserForm
from testapp.models import contactus
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

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
    # form=contactusform()
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        subject=request.POST.get("subject")
        message=request.POST.get("message")
        contact_entry=contactus(name=name,email=email,subject=subject,message=message)
        contact_entry.save()

        #send email notification  
        send_mail(
            subject,
            f'From:{name} <{email}>\n\n{message}',
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False
                    
                    )
        # Show success message
        messages.success(request, 'Your message has been sent. Thank you!')
          # Redirect back to the contact page
        return redirect('contact')  # Adjust the URL name as per your URL configuration
            
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

