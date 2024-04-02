from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'dengue/home.html')

def login(request):
    return render(request,'dengue/login.html')
