from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    time_limit_minutes = models.IntegerField(default=5, help_text="Duration of the quiz for this category in minutes")

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='questions')
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
