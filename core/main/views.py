from django.shortcuts import render, redirect
from users.models import CustomUser

from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm



def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request=request, template_name="main/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")

def index(reuqest):
    return render(reuqest, "main/index.html")



def change_user(request):
    error = ""
    if request.method == "POST":
        user = CustomUser.objects.get(username=request.user.username)
        
        new_username = request.POST.get("username")
        new_email = request.POST.get("useremail")
        new_avatar = request.FILES.get("useravatar")
        
        new_username = new_username.strip()
        new_email = new_email.strip()

        
        if new_email:
            print(f"{new_email=}", type(new_email))
            try:
                validate_email(new_email)
            except ValidationError:
                error = "Email Error"
                return render(request, "main/change_user.html", context = {"error": error})
            
            if CustomUser.objects.filter(email=new_email).exists():
                error = "Emaily arden zbaxvac a"
                return render(request, "main/change_user.html", context = {"error": error})
            else:
                if new_email:
                    user.email = new_email
            
        


        if CustomUser.objects.filter(username=new_username).exists():
            error = "Anuny Zbaxvac a"
            return render(request, "main/change_user.html", context = {"error": error})
        else:
            if new_username:
                user.username = new_username
        
            
        
        
        
        if new_avatar:
            user.avatar = new_avatar    
        
        user.save()
        
        return redirect("index")
        
    return render(request, "main/change_user.html", context = {"error": error})