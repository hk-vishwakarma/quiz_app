from django.db import models

# Create your models here.
# for questions 
class Question(models.Model):
    question_text = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text

# for answer
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=255)
    is_true = models.BooleanField(default=False)
