from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm


def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def category(request,category):
    category=category.replace('-',' ')

    try:
        category_exist=Category.objects.get(name=category)
        products = Product.objects.filter(category=category_exist)
    except:
        messages.success(request, "That category does not exist.")
        return redirect('home')
    return render(request, 'category.html', {'products': products,'category':category_exist})

def about(request):
    return render(request, 'about.html', {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect('home')
        else:
            messages.success(request, "There was an error.")
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password1)
            login(request, user)
            messages.success(request, "You have successsfully registered")
            return redirect('home')
        else:
            messages.success(request, "Undefined error. Please try again later.")
            return redirect('register')
    else:
        return render(request, 'register.html', {"form": form})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')

def product(request,pk):
    product=Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product})
