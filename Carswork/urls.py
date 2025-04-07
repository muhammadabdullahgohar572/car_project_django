
from django.urls import path
from . import views
urlpatterns = [
   path('', views.Homepage, name="Home_page"),
   path('Register/', views.Register_view, name="Register_view"),
   path('Logout/', views.Logout, name="Logout"),
   path('Login_view/',views.Login_view,name="Login_view")
]