from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra=0

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'quest_number')
    fields=['question_text', 'quest_number']
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)


