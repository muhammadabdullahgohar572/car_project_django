from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Car
from django.contrib.auth.decorators import login_required

def Homepage(request):
    carData = Car.objects.all()
    return render(request, "Home.html", {"carData": carData})

def Register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("Home_page")
    else:
        form = UserCreationForm()
    
    return render(request, "auth/Register.html", {"form": form})


def Login_view(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
          user=form.get_user()
          login(request,user)
          return redirect("Home_page")
    else:
        form = AuthenticationForm()
    
    return render(request, "auth/Login.html", {"form": form})  


def Logout(request):
    logout(request)
    return redirect("Home_page")

@login_required
def AddCar(request):
    if request.method=="POST":
        title=request.POST.get("title")
        description=request.POST.get("description")
        started_bid=request.POST.get("started_bid")
        end_auction=request.POST.get("end_auction")
        image=request.FILES.get("image");
        Car.objects.create(
            title=title,
            description=description,
            started_bid=started_bid,
            end_auction=end_auction,
            image=image,
            owner=request.user
        )
        
        
        
    return render(request,"Addcar.html")