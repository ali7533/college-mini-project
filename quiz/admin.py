from django.contrib import admin
from .models import Question, Choice, QuizSettings

# Register your models here.

# Define an inline admin descriptor for Choice model
# which acts a bit like a singleton
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# Define the admin class for Question model
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['text']}),
    ]
    inlines = [ChoiceInline]
    
    # helper to display choices in list view
    list_display = ('text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['text']

# Customize QuizSettings Admin to be more user friendly (maybe singleton style)
class QuizSettingsAdmin(admin.ModelAdmin):
    # If we want to prevent adding more than one
    def has_add_permission(self, request):
        # check if instance exists
        if QuizSettings.objects.exists():
            return False
        return True

admin.site.register(Question, QuestionAdmin)
admin.site.register(QuizSettings, QuizSettingsAdmin)
