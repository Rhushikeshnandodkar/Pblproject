from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    books_object = Book.objects.all()
    return render(request, "index.html", {'books':books_object})

def bookdetail(request, pk):
    detail_object = Book.objects.filter(book_id=pk)
    context = {'detail':detail_object}
    return render(request, "bookdetails.html", context)