from django.shortcuts import render,redirect
from .forms import UserForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=='POST':
        register_form = UserForm(request.POST)
        if register_form.is_valid:
            register_form.save()
            messages.success(request,('Register Successfully, Log in your account'))
            return redirect("register")
    else:    
        register_form = UserForm()
    context={
        'register_form':register_form
    }
    return render(request,"register.html",context)
