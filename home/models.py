from django.db import models
from tinymce import models as tinymce_models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.db.models.signals import pre_save
from URights.utils import piece_slug_generator,issue_slug_generator,news_slug_generator



class Slider(models.Model):
    slider_image=models.ImageField(upload_to="slider images")
    paragraph=models.TextField()
    attribution=models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural="Slider"
        
    def __str__(self):
        return self.paragraph[:50]


class Issue(models.Model):
    issue_title=models.CharField(max_length=200)
    publication_date=models.DateTimeField()
    cover=models.ImageField(upload_to="Issue Cover Images")
    slug=models.SlugField(blank=True)
    
    def __str__(self):
        return self.issue_title
    

class Category(models.Model):
    category_name=models.CharField(max_length=200)
    category_cover=models.ImageField(upload_to="category covers")
    
    class Meta:
        verbose_name_plural="Categories"
        
    def __str__(self):
        return self.category_name



choices=(('Draft','Draft'),('Published','Published'))    
class Piece(models.Model):
    title=models.CharField(max_length=300)
    author=models.CharField(max_length=200)
    date_modified=models.DateTimeField(auto_now=True)
    content=tinymce_models.HTMLField()
    author_bio=tinymce_models.HTMLField()
    issue=models.ForeignKey(Issue,on_delete=models.CASCADE,related_name="pieces")
    category=models.ForeignKey(Category, verbose_name="categories", on_delete=models.CASCADE,related_name="pieces")
    slug=models.SlugField(blank=True)
    status=models.CharField(choices=choices,max_length=200,default='Published')
    featured=models.BooleanField(default=False)
    
    def clean(self, *args, **kwargs):
        featured_works=Piece.objects.filter(featured=True)
        try:
            current_piece=Piece.objects.get(pk=self.pk)
        except:
            current_piece=None
        if (self.featured == True and featured_works.count() >= 3 and current_piece not in featured_works):
            raise ValidationError('Three pieces are already set as featured')
        super().clean(*args, **kwargs)
    
    def __str__(self):
        return self.title
    

class Masthead(models.Model):
    full_name=models.CharField(max_length=200)
    photo=models.ImageField(upload_to="editor photos")
    editor_bio=tinymce_models.HTMLField()
    
    class Meta:
        verbose_name_plural="Masthead"
    
    def __str__(self):
        return self.full_name
    
    
class News(models.Model):
    caption=models.CharField(max_length=200)
    date=models.DateField(auto_now_add=True)
    content=tinymce_models.HTMLField()
    slug=models.SlugField(blank=True)
    
    class Meta:
        verbose_name_plural="News"
    
    def __str__(self):
        return self.caption
    
class Newsletter(models.Model):
    full_name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.full_name} | {self.email}"
    
    class Meta:
        verbose_name='Newsletter Subscription'


class ContactForm(models.Model):
    full_name=models.CharField(max_length=200)  
    email=models.EmailField()
    message=models.TextField()  
    
    class Meta:
        verbose_name="Contact Form Data"
        verbose_name_plural="Contact Form Data"
        
    def __str__(self):
        return f"{self.full_name} | {self.email}"

class About(models.Model):
    heading=models.CharField(max_length=200)
    content=tinymce_models.HTMLField()
    
    class Meta:
        verbose_name_plural="About"
        
    def __str__(self):
        return "About Page"
    
    
class Submission(models.Model):
    heading=models.CharField(max_length=200)
    content=tinymce_models.HTMLField()
    
    class Meta:
        verbose_name_plural="Submission"
        
    def __str__(self):
        return "Submission Page"
    
    
class Poet(models.Model):
    poet_name=models.CharField(max_length=200)
    photo=models.ImageField(upload_to="Poets Photos")
    issue=models.ForeignKey(Issue,on_delete=models.CASCADE,related_name='poets')
    
    def __str__(self):
        return self.poet_name
    
    
def slug_generator(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=piece_slug_generator(instance)
        
def slug_generator_i(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=issue_slug_generator(instance)
        
def slug_generator_n(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=news_slug_generator(instance)
        
        
pre_save.connect(slug_generator,sender=Piece)
pre_save.connect(slug_generator_i,sender=Issue)
pre_save.connect(slug_generator_n,sender=News)