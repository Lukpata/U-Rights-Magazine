import string 
from django.utils.text import slugify 
import random 
  
def random_string_generator(size = 10, chars = string.ascii_lowercase + string.digits): 
    return ''.join(random.choice(chars) for _ in range(size)) 
  
def piece_slug_generator(instance, new_slug = None): 
    if new_slug is not None: 
        slug = new_slug 
    else: 
        slug = slugify(f"{instance.issue.issue_title} {instance.title}",allow_unicode=True) 
    Klass = instance.__class__ 
    qs_exists = Klass.objects.filter(slug = slug).exists() 
    if qs_exists: 
        new_slug = "{slug}-{randstr}".format( 
            slug = slug, randstr = random_string_generator(size = 4)) 
              
        return piece_slug_generator(instance, new_slug = new_slug) 
    return slug 


def book_slug_generator(instance, new_slug = None): 
    if new_slug is not None: 
        slug = new_slug 
    else: 
        slug = slugify(f"{instance.book_title} by {instance.author}",allow_unicode=True) 
    Klass = instance.__class__ 
    qs_exists = Klass.objects.filter(slug = slug).exists() 
    if qs_exists: 
        new_slug = "{slug}-{randstr}".format( 
            slug = slug, randstr = random_string_generator(size = 4)) 
              
        return piece_slug_generator(instance, new_slug = new_slug) 
    return slug 




def issue_slug_generator(instance, new_slug = None): 
    if new_slug is not None: 
        slug = new_slug 
    else: 
        slug = slugify(instance.issue_title) 
    Klass = instance.__class__ 
    qs_exists = Klass.objects.filter(slug = slug).exists() 
    if qs_exists: 
        new_slug = "{slug}-{randstr}".format( 
            slug = slug, randstr = random_string_generator(size = 4)) 
              
        return piece_slug_generator(instance, new_slug = new_slug) 
    return slug 

def news_slug_generator(instance, new_slug = None): 
    if new_slug is not None: 
        slug = new_slug 
    else: 
        slug = slugify(f"{instance.caption}-{instance.date.strftime('%d %m %Y')}") 
    Klass = instance.__class__ 
    qs_exists = Klass.objects.filter(slug = slug).exists() 
    if qs_exists: 
        new_slug = "{slug}-{randstr}".format( 
            slug = slug, randstr = random_string_generator(size = 4)) 
              
        return piece_slug_generator(instance, new_slug = new_slug) 
    return slug 

# This function for equality of passwords
def checkPassword(password1,password2):
    if password1.strip()==password2.strip():
        return True
    else:
        return False
    

#This function checks for blank fields  
def checkFields(*args):
    for field in args:
        if len(field.strip())==0:
            return False
    return True
