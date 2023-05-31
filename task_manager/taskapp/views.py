from django.shortcuts import render,redirect
from.models import FbModel
from.models import CreateModel
from django.contrib.auth.models import User


def home(request):
	request.session.modified = True
	if request.user.is_authenticated and "name" in request.session:
		user = request.user
		return render(request,"home.html")

	else:
		return redirect("ulogin")




def feedback(request):

	if request.method == "POST":
		na = request.POST.get("name")
		ema = request.POST.get("email")
		fb = request.POST.get("feedback")
		data = FbModel(name=na ,email=ema, feedback=fb)
		data.save()
		return render(request, "feedback.html" , {"msg":"Thankyou For Your FeedBack"})

	else:
		
		return render(request, "feedback.html" )

def create(request):
	if request.method == "POST":
		
		np = request.POST.get("task")
		data = CreateModel(task=np,usr_id = request.user.id)
		data.save()
		return render(request,"create.html",{"msg":"Task Added To Your List"})
		
	else:
		return render(request, "create.html")
		
	
def view(request):
	data = CreateModel.objects.filter(usr_id = request.user.id)
	return render(request, "view.html",{'data':data})

def delete(request,id):
	st = CreateModel.objects.get(pk=id)
	st.delete()
	return redirect('view')

	



