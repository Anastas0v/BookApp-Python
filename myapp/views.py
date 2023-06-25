from django.shortcuts import render
from .models import Book

# Create your views here.
def home(request):
    recommended_books = Book.objects.filter(recommended_books = True)
    fictial_books = Book.objects.filter(fictial_books = True)
    business_books = Book.objects.filter(business_books = True)
    return render(request, 'home.html', {'recommended_books': recommended_books, 'bussiness_books': business_books, 'fictial_books': fictial_books})

def all_books(request):
    books = Book.objects.all()
    return render(request, 'all_books.html', {'books':books})