from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User

def index(request):
    category = Category.objects.all()
    products = Product.objects.all()
    context = {
        "category": category,
        "products": products
    }
    return render(request, 'pages/index.html', context)

def detail(request, p_id):
    category = Category.objects.all()
    product = Product.objects.get(id=p_id)
    context = {
        "category": category,
        "product" : product
    }
    return render(request, 'pages/detail.html', context)

def category(request, c_id):
    category = Category.objects.all()
    c = Category.objects.get(id=c_id)
    products = Product.objects.filter(category=c)
    context = {
        "category": category,
        'products': products,
        'c': c,
        
    }
    return render(request, 'pages/category.html', context)

def search(request):
    if request.method == "POST":
        category = Category.objects.all()
        products = Product.objects.filter(title__icontains=request.POST['title'])
        context = {
            "category": category,
            "products": products
        }
    return render(request, 'pages/search.html', context)


# LOGIN
def login(request):
    category = Category.objects.all()
    context = {
        "category": category
    }
    return render(request, 'pages/login.html', context)

def reg(request):
    category = Category.objects.all()
    context = {
        "category": category
    }
    return render(request, 'pages/register.html', context)


def reg_create(request):
    if request.method == "POST":
        # users_arr = []
        # users = User.objects.all()
        # for i in users:
        #     users_arr.append(i.username)

        users_arr = list(map(lambda x: x.username, User.objects.all()))
        if request.POST['username'].lower() in users_arr:
            return redirect('reg')

        users_emails = list(map(lambda x: x.email, User.objects.all()))
        if request.POST['email'].lower() in users_emails:
            return redirect('reg')

        users_phone = list(map(lambda x: x.last_name, User.objects.all()))
        if request.POST['phone'].lower() in users_phone:
            return redirect('reg')

        User.objects.create_user(
            username = request.POST['username'].lower(),
            password = request.POST['password'],
            first_name = request.POST['name'],
            last_name = request.POST['phone'],
            email = request.POST['email'].lower()
        )
        return redirect('login')



def tekshirish(request):
    if request.method == "POST":
        username = request.POST['username'].lower()
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('control')
        return redirect('login')

def logout(request):
    auth.logout(request)
    return redirect('login')

