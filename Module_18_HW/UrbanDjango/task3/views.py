from django.shortcuts import render

def platform(request):
    return render(request, 'third_task/platform.html')

def games(request):
    return render(request, 'third_task/games.html')

def cart(request):
    return render(request, 'third_task/cart.html')