from django.shortcuts import render,redirect 
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.contrib import messages
from books.models import Book,Order,OrderItem
from django.contrib.auth.decorators import login_required
from datetime import timedelta
from django.utils import timezone

# Create your views here.

def personal(request):
    return render(request, "personal.html")


def password(request):

    if request.method == 'POST':

        password1 = request.POST['password1']
        password2 = request.POST['password2']
        password3 = request.POST['password3']

        if request.user.is_authenticated:
            email = request.user.get_username()
            a = auth.authenticate(username = email,password = password1)

            if a is not None:
                if(password2 == password3) :
                    request.user.set_password(password2)
                    request.user.save()
                    messages.info(request, "Password updated.")
                    return render(request, "password.html")
                else:
                    messages.info(request, "Passwords Dont match.")
                    return render(request, "password.html")
            else:
                messages.info(request, "Check credentials.")
                return render(request, "password.html")
    else:
        return render(request, "password.html")

@login_required
def old_orders(request):

    orders = Order.objects.filter(user = request.user, ordered=True)

    if orders:
        return render(request,'old_orders.html',{'orders':orders})
    else:
        return render(request,'old_orders.html')

def retrn(request,id):
    order = Order.objects.get(id = id)
    date_start = order.ordered_date
    date_end = date_start + \
        timedelta(days=30)
    date_now = timezone.now()
    if date_now <= date_end:
        messages.success(request,"Return initiated")
        order.return_started = True
        order.save()
        return redirect('old_orders')
    else:
        messages.success(request,"Return cannot be initiated. Time is crossed")
        return redirect('old_orders')

def my_books(request):
    books = Book.objects.filter(merchant = request.user)
    return render(request,'my_books.html',{'books':books})