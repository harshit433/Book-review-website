from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegisterForm, LoginForm, BookForm
from .models import Book, Review
from django.db.models import Avg, Sum, Min, Max, Count, Func
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import ReviewForm

class Round(Func):
    function = 'ROUND'
    template='%(function)s(%(expressions)s, 2)'

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
            print("Logged in")
    else:
        form = UserRegisterForm()
        print("reequest else")
    return render(request, 'reviews/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
            else:
                print("No user found")
    else:
        form = LoginForm()
    return render(request, 'reviews/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def home(request):
    books = Book.objects.all()
    return render(request, 'reviews/home.html', {'books': books})


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return redirect('home')  # Change 'book_list' to the name of your book list view
    else:
        form = BookForm()
    return render(request, 'reviews/add_book.html', {'form': form})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    all_reviews = book.reviews.all()
    average = all_reviews.aggregate(latest = Round(Avg('rating')))
    diction = []
    if(average['latest'] is None):
        average['latest'] = 0
    
    for i in range(5):
        if( i < average['latest']):
            diction.append('fa fa-star checked')
        else:
            diction.append('fa fa-star unchecked')
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.reader = request.user
            review.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = ReviewForm()
    return render(request, 'reviews/book_detail.html', {'book': book, 'average_rating': diction, 'form': form})