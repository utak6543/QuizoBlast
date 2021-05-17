from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Subject(models.Model):

    def __str__(self):
        return self.name

    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='sub_images',default='media/sub_images/default_sub.jpg')
    description=models.TextField(max_length=1500)

class QandA(models.Model):

    def __str__(self):
        return self.question

    sub=models.ForeignKey(Subject,on_delete=models.CASCADE)
    question=models.CharField(max_length=400)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)

class Score(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    sub=models.ForeignKey(Subject,on_delete=models.CASCADE)
    marks=models.IntegerField(default=0)
