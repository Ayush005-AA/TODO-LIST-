
from django.urls import path 
from todoapp import views

urlpatterns = [
    path("",views.home ,name="home"),
    path("showdata",views.showdata,name="showdata"),
    path("remove/<int:id>",views.remove,name = "remove"),
    path("update/<int:id>",views.update,name = "update"),
    path("signup/",views.signup,name = "signup"),
    path("login/",views.loginfunction,name = "loginn"),
   
]