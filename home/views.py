from django.shortcuts import render,redirect
from .models import Slider,Issue,Poet,Piece,News,ContactForm,Newsletter,Category
from URights.utils import checkFields
from django.contrib import messages
from django.db.models import Q

def home_page(request):
    sliders=Slider.objects.all()
    featured_cats=Category.objects.all()[:4]
    featured_poets=Poet.objects.all()[:7]
    featured_pieces=Piece.objects.filter(featured=True)
    context={'sliders':sliders,'featured_pieces':featured_pieces,'featured_poets':featured_poets,'featured_cats':featured_cats}
    return render(request,'index.html',context)

def search_func(request):
    search_value=request.GET.get('search_value',"")
    if search_value:
        pieces=Piece.objects.filter(status="Published")
        search_query=pieces.filter(Q(title__icontains=search_value) | Q(author__icontains=search_value))
        piece_count=search_query.count()
        context={'search_results':search_query, 'search_value':search_value,'piece_count':piece_count}
        return render(request,'search.html',context)
    return render(request,'search.html')


def page(request,template,model):
    items=model.objects.all()
    context={f"{model.__name__.lower()}_items":items}
    return render(request,template,context)

def our_poets(request):
    issues=Issue.objects.all()
    poets=Poet.objects.all()
    context={'issues':issues,'poets':poets}
    return render(request,'our-writers.html',context)

def issue_content(request,slug):
    issue=Issue.objects.get(slug=slug)
    pieces=issue.pieces.filter(status='Published')
    context={'issue':issue,'pieces':pieces}
    return render(request,'general-issue-content.html',context)

def piece_detail(request,slug):
    piece=Piece.objects.get(slug=slug)
    issue_pk=piece.issue.pk
    pieces_in_issue=Issue.objects.get(pk=issue_pk).pieces.all()
    context={'piece':piece,'issue':pieces_in_issue}
    return render(request,'detail-content.html',context)

def news_detail(request,slug):
    news=News.objects.get(slug=slug)
    context={'news':news}
    return render(request,'news-detail.html',context)

def archive(request,category):
    category=Category.objects.get(category_name=category)
    pieces=category.pieces.all()
    context={'pieces':pieces,'category':category}
    return render(request,'archive.html',context)

def contact(request):
    page='contact'
    if request.method=='POST':
        full_name=request.POST['f_name']
        email=request.POST['email']
        message=request.POST['message']
        validated=checkFields(full_name,email,message)
        if validated:
            new_contact=ContactForm(full_name=full_name,email=email,message=message)
            new_contact.save()
            return render(request,'success.html',{'page':page})
        else:
            messages.info('request','All fields must be completed')
            return redirect('home:contact')
            
    return render(request,"contact.html")

def newsletter(request):
    if request.method!='POST':
        return redirect('home:home_page')
    else:
        full_name=request.POST['full_name']
        email=request.POST['email']
        validated=checkFields(full_name,email)
        if validated:
            subscriber=Newsletter(full_name=full_name,email=email)
            subscriber.save()
            messages.info(request,'Details submitted successfully')
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.info(request,'All fields must be completed')
            return redirect(request.META['HTTP_REFERER'])

