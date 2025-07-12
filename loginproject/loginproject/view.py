from django.shortcuts import render

def home(request):
    return render(request, 'HTML/front.html')


def signin(request):
    return render(request, 'HTML/signin.html')

def signup(request):
    return render(request, 'HTML/signup.html')




