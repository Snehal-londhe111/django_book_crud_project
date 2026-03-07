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