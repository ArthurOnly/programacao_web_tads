from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    description = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)

class Author(models.Model):
    profile = models.ForeignKey(Profile, on_delete = models.PROTECT)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

class Tag(models.Model):
    title = models.CharField(max_length=50)
    color = models.CharField(max_length=7)

    class Meta:
        verbose_name = "Rótulo"

    def __str__(self):
        return self.title

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Data de publicação')
    end_date = models.DateTimeField('Data de encerramento', null = True)
    active = models.BooleanField("Ativo")
    tags = models.ManyToManyField(Tag, verbose_name="Tags", null=True, blank=True)
    author = models.ForeignKey(Author, on_delete = models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Enquete"

    def __str__(self):
        return f"{self.question_text}"

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Opção"

    def __str__(self):
        return f"{self.choice_text}"


