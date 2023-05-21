from django.contrib import admin
from .models import Question, Choice


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [

        ('faaltu kam', {'fields': ['q_text']}),
        ('Date information', {'fields': ['pub_date']})

    ]
    inlines = [ChoiceInLine]
    list_display = ('q_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['q_text']


admin.site.register(Question, QuestionAdmin)

# Register your models here.
