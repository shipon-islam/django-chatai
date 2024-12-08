from django.shortcuts import render

# Create your views here.


def home(request):
    print(request.path)
    return render(request, 'home.html')


def pricing(request):
    return render(request, 'pricing.html')
