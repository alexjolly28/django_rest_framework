from django.db import models


class Quiz(models.Model):
    name = models.CharField(max_length=200)
    disc = models.TextField(verbose_name='discription', null=True)
    date = models.DateField(auto_now=True)


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    ques = models.TextField(verbose_name='question', null=False)
    answer = models.TextField(verbose_name='answer', null=False)
