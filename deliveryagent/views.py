from django.shortcuts import render,redirect,get_object_or_404
from books.models import Book,OrderItem,Order
from django.contrib import messages
from django.conf import settings


# Create your views here.

def home_d(request):

    orders = Order.objects.filter(ordered=True,delivered = False)

    if orders:
        return render(request,'home_d.html',{'orders':orders})
    else:
        return render(request,'home_d.html')

def accpetd(request,id):
    order = Order.objects.get(id = id)
    order.dely = True
    order.save()
    messages.success(request,"Order Accepted")
    return redirect('home_d')


def delivd(request,id):
    order = Order.objects.get(id = id)
    order.delivered = True
    order.save()
    messages.success(request,"Order Delivered")
    return redirect('home_d')


def retrn_reqd(request):

    orders = Order.objects.filter(ordered=True,return_started = True,returned = False)

    if orders:
        return render(request,'retrn_reqd.html',{'orders':orders})
    else:
        return render(request,'retrn_reqd.html')

def accptd_rtn(request,id):
    order = Order.objects.get(id = id)
    order.return_accepted = True
    order.save()
    messages.success(request,"Order Accepted")
    return redirect('retrn_reqd')

def delivd_rtn(request,id):
    order = Order.objects.get(id = id)
    order.returned= True
    order.save()
    messages.success(request,"Return Taken")
    return redirect('retrn_reqd')
