from django.contrib import admin

from .models import Question, Choice

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra=2

class QuestionAdmin(admin.ModelAdmin):
    fields=['question_text', 'quest_number']
    inlines = [ChoiceInline]
    list_display = ('question_text', 'quest_number')

admin.site.register(Question, QuestionAdmin)


