from django.shortcuts import render,redirect

from .models import *

# Create your views here.
def InsertView(request):
    return render(request, "bookapp/insert.html")

def InsertData(request):
    bn = request.POST['bname']
    ba = request.POST['bauthor']
    bpge = request.POST['bpage']
    bpz = request.POST['bprice']

    all_book = Book.objects.create( Bookname = bn,
                                   Bookauthor = ba,
                                   Bookpage = bpge,
                                   Bookprice = bpz
                                   )
    return redirect('showdata')

def ShowData(request):
    show_book = Book.objects.all()
    return render(request, "bookapp/show.html", {'key1':show_book})

def EditView(request,pk):
    get_book = Book.objects.get(id=pk)
    return render(request, "bookapp/edit.html",{'key2':get_book})

def UpdateData(request,pk):
    bdata = Book.objects.get(id=pk)

    bdata.Bookname = request.POST['bname']
    bdata.Bookauthor = request.POST['bauthor']
    bdata.Bookpage = request.POST['bpage']
    bdata.Bookprice = request.POST['bprice']

    bdata.save()
    return redirect('showdata')

def DeleteData(request,pk):
    ddata = Book.objects.get(id=pk)
    ddata.delete()
    return redirect('showdata')