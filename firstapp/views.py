from django.shortcuts import render,HttpResponse
from django.views import View



# Create your views here.

def home(request):
    return HttpResponse("First view")

def firstpage(request):
    return HttpResponse("<h1>First Page</h1>")

def about(request):
    return HttpResponse("My name is Nihal Ruke. I am 23 years old I stay in vakola Santacruz(east) Mumbai 40092")

def contact(request):
    return HttpResponse("Contact no: 9529034574")
    
def contact(request):
    return HttpResponse("Mail id: nihalruke1232001@gmail.com")
    
def users(request):
    student={
        "id":100,
        "Name":"Nihal",
        "age":23
    }
    return render(request,"index.html",student)

def register(request):
    return render(request,"register.html")

def submit(request):
    if request.method=="POST":
        return render(request,"submit.html")
    if request.method=="GET":
        return render(request,"register.html")
    
#Class based view
class firstView(View):
    def get(self,request):
        return HttpResponse("Class Based View -GET")
    
class secondView(View):
    name="Sai"
    def get(self,request):
        return render(request,"detail.html",{"name":self.name})
