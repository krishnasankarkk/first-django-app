from django.contrib import admin

from .models import Question, Choice

# admin.site.register(Question)
# admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    # fields = [ "pub_date", "question"]
    fieldsets = [
        (None, {"fields": ["question"]}),
        ("Date Information", {"fields": ["pub_date"]}),
    ]
    list_display = ["question", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question"]
    inlines = [ChoiceInline]
    
admin.site.register(Question, QuestionAdmin)