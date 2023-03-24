from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_models
from datetime import date
from django.utils.text import slugify
from django.db.models.signals import pre_save
from URights.utils import book_slug_generator,issue_slug_generator,news_slug_generator



class AuthorProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    country=models.CharField(max_length=200)
    bio=tinymce_models.HTMLField()
    
    def __str__(self):
        return self.user.username

choices=(('approved','approved'),('pending','pending'))
class Book(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book_title=models.CharField(max_length=200)
    publisher=models.CharField(max_length=200)
    isbn=models.CharField(max_length=200,null=True,blank=True)
    author=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    year=models.IntegerField()
    pages=models.IntegerField()
    plan=models.CharField(max_length=100,default='free')
    price=models.IntegerField(null=True,blank=True)
    url=models.URLField(blank=True,null=True)
    excerpt=tinymce_models.HTMLField()
    book_cover=models.FileField(upload_to='book covers')
    slug=models.SlugField(null=True,blank=True)
    status=models.CharField(choices=choices,default='pending',max_length=200)
    approval_date=models.DateField(default=date.today)
    
    def __str__(self) -> str:
        return f"{self.book_title}|{self.author}"
    
    def save(self,*args,**kwargs):
        if self.price=="":
            self.price=0
        super().save(*args,**kwargs)
        
    class Meta:
        ordering=['-approval_date',]
        
        
class Order(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    no_of_copies=models.IntegerField()
    email=models.EmailField()
    message=models.TextField()
    order_date=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=200,choices=(('pending','pending'),('treated','treated')),default='pending')
    
    def __str__(self):
        return f"{self.name} ordered {self.book.book_title}"
    
    class Meta:
        ordering=['-order_date',]
        verbose_name='Book Order'
    
    
    
def slug_generator(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=book_slug_generator(instance)
        

pre_save.connect(slug_generator,sender=Book)