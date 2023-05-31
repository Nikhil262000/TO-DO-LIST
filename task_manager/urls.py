
from django.contrib import admin
from django.urls import path
from taskapp.views import home,feedback,create,view,delete
from auapp.views import usignup,ulogin,ulogout,resetpassword

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path("usignup/",usignup,name="usignup"),
    path("ulogin/",ulogin,name="ulogin"),
    path("ulogout/",ulogout,name="ulogout"),   
    path("resetpassword/",resetpassword,name="resetpassword"),
    path("feedback/",feedback,name="feedback"),
    path("create/",create, name="create"),
    path("view/",view, name="view"),
    path("delete/<int:id>",delete, name="delete"),
]
