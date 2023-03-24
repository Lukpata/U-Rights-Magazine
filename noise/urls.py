
from django.urls import path
from .views import noise_home,noise_submit,noise_issue

app_name='noise'

urlpatterns = [
    path('',noise_home,name='noise_home'),
    path('issues/<str:slug>/',noise_issue,name='issue'),
    path('submit',noise_submit,name='noise_submit'),
]