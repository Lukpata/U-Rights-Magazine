from django.db import models
from tinymce import models as tinymce_models

class Issue(models.Model):
    issue_number=models.CharField(max_length=200)
    issue_title=models.CharField(max_length=200)
    publication_date=models.DateTimeField()
    issue_cover=models.ImageField(upload_to="Noise Issue Cover")
    slug=models.SlugField()
    cover_anotation=models.CharField(max_length=200, default="Joseph Mills")
    
    class Meta:
        ordering=['-publication_date',]
    
    def __str__(self):
        return self.issue_number
    
class Poem(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    content=tinymce_models.HTMLField()
    author_bio=tinymce_models.HTMLField()
    issue=models.ForeignKey(Issue,on_delete=models.CASCADE,related_name="pieces")
    date_modified=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    
class Submission(models.Model):
    issue_title=models.CharField(max_length=200)
    theme_exposition=tinymce_models.HTMLField()
    guidelines=tinymce_models.HTMLField()
    about_noise=tinymce_models.HTMLField()
    
    class Meta:
        verbose_name_plural="Submission"
        
    def __str__(self) -> str:
        return "submission"
    
