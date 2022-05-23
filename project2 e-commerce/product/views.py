from django.shortcuts import render,redirect
from .models import category,product,cart
def home(request):
    allcategory = category.objects.all()
    allproducts = product.objects.all()
    number =cart.objects.all().count()
    return render(request,'pages/home.html',{"allproducts":allproducts,"allcategory":allcategory,'number':number})

def Category(request,categoryid):
    allcategory = category.objects.all()
    mycategory = category.objects.get(id=categoryid)
    allproducts = product.objects.all().filter(category_id = categoryid )
    number =cart.objects.all().count()
    return render(request,'pages/category.html',{"allproducts":allproducts,'number':number,"allcategory":allcategory,"mycategory":mycategory})


def Product(request,productid):
    allcategory = category.objects.all()
    myproduct = product.objects.get(id=productid)
    number =cart.objects.all().count()
    return render(request,'pages/product.html',{"allcategory":allcategory,'number':number,"myproduct":myproduct})

def newproducts(request):
    allcategory = category.objects.all()
    allproducts = product.objects.all().order_by("-id")
    number =cart.objects.all().count()
    return render(request,'pages/newproducts.html',{"allproducts":allproducts,'number':number,"allcategory":allcategory})

def carti(request):
    allcategory = category.objects.all()
    allproducts = product.objects.all()
    number =cart.objects.all().count()
    carts=cart.objects.all()
    return render(request,'pages/cart.html',{'cart':carts,"allproducts":allproducts,'number':number,"allcategory":allcategory})



def add(request,productid):
    a=int(cart.objects.filter(prodd=productid).count())
    if a >= 1:
        s=cart.objects.get(prodd=productid)
        cart.objects.filter(prodd=productid).update(numb=int(s.numb)+1)
    else:
        carts=cart(prodd=productid,numb=1)
        carts.save()
    return redirect("/")