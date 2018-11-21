from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=60)
    closed = models.BooleanField(default=False)
    pub_date = models.DateField()

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=30)
    votes = models.IntegerField()

    def __str__(self):
        return self.choice_text

    def votar(self):
        self.votes += 1
        self.votes.save()



