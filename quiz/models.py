from django.db import models

# Model representing a Quiz Question
class Question(models.Model):
    # The text of the question, limited to 200 characters
    text = models.CharField(max_length=200)
    # The date and time the question was published, automatically set when created
    pub_date = models.DateTimeField(auto_now_add=True)

    # String representation of the Question object (shows the question text)
    def __str__(self):
        return self.text

# Model representing a specific choice/answer for a question
class Choice(models.Model):
    # Foreign key linking the choice to a specific Question. 
    # If the Question is deleted, all associated Choices are also deleted (CASCADE).
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    # The text of the choice/answer
    text = models.CharField(max_length=200)
    # Boolean flag to indicate if this choice is the correct answer
    is_correct = models.BooleanField(default=False)

    # String representation of the Choice object
    def __str__(self):
        return self.text

# Singleton model for Quiz Settings
class QuizSettings(models.Model):
    time_limit_minutes = models.IntegerField(default=5, help_text="Duration of the quiz in minutes")

    class Meta:
        verbose_name_plural = "Quiz Settings"

    def __str__(self):
        return f"Quiz Settings ({self.time_limit_minutes} min)"

    def save(self, *args, **kwargs):
        # validation to ensure only one instance exists (optional but good practice)
        if hasattr(self, 'pk') and self.pk is not None:
             super(QuizSettings, self).save(*args, **kwargs)
        else:
             if not QuizSettings.objects.exists():
                 super(QuizSettings, self).save(*args, **kwargs)
             else:
                 # If we want to strictly enforce one, we could raise error or update existing.
                 # For simplicity, we'll just update the first one if someone tries to create another
                 # via code, but admin enforces via permissions usually.
                 existing = QuizSettings.objects.first()
                 existing.time_limit_minutes = self.time_limit_minutes
                 existing.save()
