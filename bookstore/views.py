from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from URights.utils import checkFields,checkPassword
from .models import AuthorProfile,Book,Order
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Q

def bookstore(request):
    books=Book.objects.filter(status='approved')
    search_query=request.GET.get('book_search','')
    if search_query:
        books=books.filter(Q(book_title__icontains=search_query) | Q(author__icontains=search_query))
    context={'books':books,'search_value':search_query}
    return render(request,'bookstore-home.html',context)

def book_info(request,slug):
    book=Book.objects.get(slug=slug)
    context={'book':book}
    return render(request,'book-detail.html',context)

def order_book(request,slug):
    book=Book.objects.get(slug=slug)
    page="order"
    if request.method=='POST':
        name=request.POST['fullName']
        copies=request.POST['copies']
        email=request.POST['email']
        message=request.POST['message']
        validated=checkFields(name,email,message)
        if validated:
            order=Order(book=book,name=name,email=email,message=message,no_of_copies=copies)
            order.save()
            return render(request,'success.html',{'page':page})
        else:
            messages.info(request,'All fields must be completed')
            return redirect(reverse('bookstore:order_book',args=book.slug))
    return render(request,'order-form.html',{'book':book})



def register(request):
    page='register'
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['firstName']
        last_name=request.POST['lastName']
        email=request.POST['email']
        password=request.POST['password']
        country=request.POST['country']
        password2=request.POST['confirmation']
        bio=request.POST['bio']
        
        if checkFields(username,first_name,last_name,email,password,password2,bio) and checkPassword(password,password2):
            if User.objects.filter(username=username).exists():
                messages.info(request,"That username is taken")
                return redirect('bookstore:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'That email is taken')
                return redirect('bookstore:register') 
            else:
                new_user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                new_user.save()
                author_profile=AuthorProfile(user=new_user,bio=bio,country=country)
                author_profile.save()
                return render(request,'success.html',{'page':page})
            
            
        elif ~checkFields(username,first_name,last_name,email,password,password2,bio) and checkPassword(password,password2):
            messages.info(request,'All the fields must be completed')
            return redirect('bookstore:register')
        
        else:
            messages.info(request,'Passwords do not match')
            return redirect('bookstore:register')
            
    else:
        return render (request,'registration.html')
    
    
def noise_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('bookstore:bookstore')
        else:
            messages.info(request,'Incorrect login credentials')
            return redirect('bookstore:login')
    else:
        return render(request,'login.html')
    
    
def noise_logout(request):
    logout(request)
    return redirect('bookstore:bookstore')

@login_required
def submit(request):
    page='submit'
    if request.method=='POST':
        book_title=request.POST['bookTitle']
        publisher=request.POST['publisher']
        isbn=request.POST['bookTitle']
        author=request.POST['author']
        category=request.POST['category']
        year=request.POST['year']
        pages=request.POST['pages']
        plan=request.POST['plan']
        price=request.POST.get('price',0.00)
        url=request.POST['url']
        excerpt=request.POST['bio']
        file=request.FILES['file']
        validated=checkFields(book_title,publisher,author,year,pages,excerpt)
        if validated:
            new_book=Book(book_title=book_title,author=author,
                          category=category,year=year,
                          pages=pages,plan=plan,price=price,
                          url=url,excerpt=excerpt,book_cover=file,
                          isbn=isbn,publisher=publisher)
            new_book.user=request.user
            new_book.save()
            return render(request,'success.html',{'page':page,'book_title':book_title})
        else:
            messages.info(request,'All required fields must be completed')
            return redirect('bookstore:submit')
        
    return render(request,'submit-a-book.html')
    
    