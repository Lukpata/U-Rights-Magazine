from django.contrib import admin
from .models import Issue,Poem,Submission

class IssueAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':['issue_number'],}

MAX_OBJECTS=1    
class SubmissionAdmin(admin.ModelAdmin):
    def has_add_permission(self, request) -> bool:
        if self.model.objects.count()>=MAX_OBJECTS:
            return False
        return super().has_add_permission(request)

admin.site.register(Issue,IssueAdmin)
admin.site.register(Poem)
admin.site.register(Submission,SubmissionAdmin)
