
from django.urls import path
from .views import bookstore,register,noise_login,noise_logout, submit,book_info,order_book

app_name='bookstore'
urlpatterns = [
    path('',bookstore,name='bookstore'),
    path('register',register,name='register'),
    path('login/',noise_login,name='login'),
    path('logout/',noise_logout,name='logout'),
    path('submit-a-book/',submit,name='submit'),
    path('book/<str:slug>/',book_info,name='book_info'),
    path('order/<str:slug>/',order_book,name='order_book')
]