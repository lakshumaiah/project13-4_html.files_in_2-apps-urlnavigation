from django.shortcuts import render

# Create your views here.
def eswar(request):
    return render(request,'eswar.html')


def laxman(request):
    return render(request,'laxman.html')    
