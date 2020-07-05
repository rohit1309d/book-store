from django.shortcuts import render,redirect,get_object_or_404
from books.models import Book,OrderItem,Order
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage


# Create your views here.

def addBook(request):
    if request.method == "POST":
        name = request.POST["name"] 
        author = request.POST["author"]
        cost = request.POST["cost"]

        uploaded_file = request.FILES["img"]
        fs = FileSystemStorage()
        img = fs.save(uploaded_file.name,uploaded_file)
        book = Book()
        if Book.objects.filter(name = name, author = author, cost= cost, merchant = request.user).exists():
            messages.info(request,"Book exists")
            return redirect("home") 
        else:
            book = Book.objects.create(name = name, author = author, cost= cost, img = img, merchant = request.user)
            book.save()
            messages.info(request,"Book Uploaded")
            return redirect("home") 
    else:
        messages.info(request,"No action")
        return redirect("home")

def book_reqm(request):

    orders = Order.objects.filter(ordered=True,delivered = False,mer = False)

    if orders:
        return render(request,'book_reqm.html',{'orders':orders})
    else:
        return render(request,'book_reqm.html')

def accpetm(request,id):
    order = Order.objects.get(id = id)
    order.mer = True
    order.save()
    messages.success(request,"Order Accepted")
    return redirect('book_reqm')