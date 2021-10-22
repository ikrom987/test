from django.shortcuts import redirect, render
from pages.models import *
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def control(request):
    category = Category.objects.all()
    products = Product.objects.filter(user=request.user)
    context = {
        "category": category,
        "products": products
    }
    return render(request, 'control/control.html', context)

@login_required(login_url='login')
def control_add(request):
    category = Category.objects.all()
    context = {
        "category": category
    }
    return render(request, 'control/add.html', context)


@login_required(login_url='login')
def control_create(request):
    if request.method == "POST" and request.FILES['file']:
        Product.objects.create(
            user=request.user,
            category_id=request.POST['category'],
            title=request.POST['title'],
            price=request.POST['price'],
            description=request.POST['info'],
            image=request.FILES['file']
        )
        return redirect('control')


@login_required(login_url='login')
def control_detail(request, id):
    product = Product.objects.get(id=id)
    category = Category.objects.all()
    context = {
        "product": product,
        "category" : category
    }
    return render(request, 'control/detail.html', context)


@login_required(login_url='login')
def control_delete(request):
    if request.method == "POST":
        p = Product.objects.get(id=request.POST['id'])
        p.delete()
    return redirect('control')