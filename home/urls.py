
from django.urls import path
from .views import home_page,page,contact,our_poets,issue_content,piece_detail,news_detail,newsletter,archive,search_func
from .models import Issue,Masthead,News,About,Submission

app_name='home'

urlpatterns = [
    path('',home_page,name='home_page'),
    path('about/',page,{'template':'about.html','model':About},name='about'),
    path('masthead/',page,{'template':'masthead.html','model':Masthead},name='masthead'),
    path('contact/',contact,name='contact'),
    path('our_poets/',our_poets,name='our_poets'),
    path('news/',page,{'template':'news-brief.html','model':News},name='news'),
    path('news/<str:slug>/',news_detail,name='news_detail'),
    path('submissions/',page,{'template':'general-submissions.html','model':Submission},name='submissions'),
    path('issues/',page,{'template':'issues-home.html','model':Issue},name='issues'),
    path('issue_content/<str:slug>/',issue_content,name='issue_content'),
    path('issue/<str:slug>/',piece_detail,name='piece_detail'),
    path('newsletter/',newsletter,name='newsletter'),
    path('archive/<str:category>/',archive,name='archive'),
    path('search/',search_func,name='search'),
]