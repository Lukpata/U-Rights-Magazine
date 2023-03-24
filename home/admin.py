from django.contrib import admin
from .models import Slider,Category,Issue,Piece,Masthead,News,About,Submission,Poet,Newsletter,ContactForm

MAX_OBJECTS=1
class PageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request) -> bool:
        if self.model.objects.count()>=MAX_OBJECTS:
            return False
        return super().has_add_permission(request)
    
    
admin.site.register(Slider)
admin.site.register(Category)
admin.site.register(Issue)
admin.site.register(Piece)
admin.site.register(Masthead)
admin.site.register(News)
admin.site.register(About,PageAdmin)
admin.site.register(Submission,PageAdmin)
admin.site.register(Poet)
admin.site.register(ContactForm)
admin.site.register(Newsletter)


