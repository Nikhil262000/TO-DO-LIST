from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import ProfileModel, MyUser
from random import randrange
from django.core.mail import send_mail



def usignup(request):
	if request.method == "POST":
		tx = request.POST.get("tx")
		em = request.POST.get("em")

		if User.objects.filter(username=tx):
			return render(request,"usignup.html",{"msg":"Username already registered"})

			
		elif User.objects.filter(email=em):
			return render(request,"usignup.html",{"msg":"Email already registered"})
		else:
			
			
			pw = ""
			text = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
			for i in range(6):
				pw = pw + text[randrange(len(text))]
			print(pw)
			subject = "welcome to Task Manager Website"
			msg = "Hello,Your password is " + str(pw)
			host = 'nikhilpatil4844@gmail.com'
			recepient = [em]
			send_mail(subject, msg, host, recepient)
			usr = User.objects.create_user(username=tx,email=em,password=pw)
			usr.save()
			return redirect("ulogin")
	else:
		return render(request,"usignup.html")

def ulogin(request):

	if request.method == "POST":
		tx = request.POST.get("tx")
		pw = request.POST.get("pw")
		usr = authenticate(username=tx,password=pw)
		if usr is not None:
			login(request,usr)
			request.session["name"] = tx
			return redirect("home")
		else:
			return render(request,"ulogin.html",{"msg":"invalid login"})
	else:
		return render(request,"ulogin.html")

def resetpassword(request):
	
	if request.method == "POST":
	
		em = request.POST.get("em")
		
		try:
			print("*" * 50)
			usr = User.objects.get(email=em)
			print(usr)
			pw = ""
			text = "0123456789abcdefghijklmnopqrstuvwxyz"
			for i in range(6):
				pw = pw + text[randrange(len(text))]
			print(pw)
			subject = "welcome to Task Manager Website"
			msg = "Hello,Your password is " + str(pw)
			host = 'nikhilpatil4844@gmail.com'
			recepient = [em]
			send_mail(subject, msg, host, recepient)
			usr.set_password(pw)

			usr.save()
			return redirect("ulogin")
		except User.DoesNotExist:
			return render(request,"resetpassword.html",{"msg":"Invalid Email"})
	else:
		return render(request,"resetpassword.html")
	

def ulogout(request):
	logout(request)
	request.session.flush()
	request.session.clear_expired()
	return redirect("ulogin")

