from django.contrib import admin
from .models import Question, Choice, Category

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['text', 'category']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('text', 'category', 'pub_date')
    search_fields = ['text']
    list_filter = ['category']

admin.site.register(Question, QuestionAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'time_limit_minutes')

admin.site.register(Category, CategoryAdmin)

