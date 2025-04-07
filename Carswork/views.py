from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Car
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now

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
        return redirect("Home_page")
    return render(request,"Addcar.html")


@login_required
def ShowDetalis(request, id):
    car = get_object_or_404(Car, id=id)
    bids=car.bids.all()
    remanining_time=max((car.end_auction - now()).total_seconds(),0)
    error_message=None,
    acution_active=remanining_time >0
    winner=0
    
    context={
        "car":car,
        "bids":bids,
        "remanining_time":remanining_time,
        "error_message":error_message,
        "acution_active":acution_active,
        "winner":winner
    }
    return render(request, "ShowDeatils.html", context)
    