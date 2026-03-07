from django.shortcuts import render

# Create your views here.
def InsertView(request):
    return render(request, "bookapp/insert.html")