from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    description = models.CharField(_("Descrição"), max_length=100)
    city = models.CharField(_("Cidade"), max_length=50)
    country = models.CharField(_("País"), max_length=50)
    gender = models.CharField(_("Gênero"), max_length=50)

    class Meta:
        verbose_name = _("Perfil de autor")
        verbose_name_plural = _("Perfis de autores")

    def __str__(self):
        return self.description

class Author(models.Model):
    name = models.CharField(_("Nome"), max_length=200)
    profile = models.ForeignKey(Profile, verbose_name=_("Perfil"), on_delete = models.PROTECT)
    user = models.ForeignKey(User, verbose_name=_("Usuário"), on_delete = models.CASCADE)

    class Meta:
        verbose_name = _("Autor")
        verbose_name_plural = _("Autores")

    def __str__(self):
        return self.name

class Tag(models.Model):
    title = models.CharField(_("Rótulo"), max_length=50)
    color = models.CharField(_("Cor"), max_length=7)

    class Meta:
        verbose_name = _("Rótulo")
        verbose_name_plural = _("Rótulos")

    def __str__(self):
        return self.title

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(_("Data de publicação"))
    end_date = models.DateTimeField(_("Data de encerramento"), null = True)
    active = models.BooleanField(_("Ativo"))
    tags = models.ManyToManyField(Tag, verbose_name=_("Tags"), blank=True)
    author = models.ForeignKey(Author, verbose_name=_("Autor"), on_delete = models.CASCADE, null=True)

    class Meta:
        verbose_name = _("Enquete")
        verbose_name_plural = _("Enquetes")

    def __str__(self):
        return f"{self.question_text}"

class Choice(models.Model):
    question = models.ForeignKey(Question, verbose_name=_("Questão"), on_delete = models.CASCADE)
    choice_text = models.CharField(_("Descrição da alternativa"), max_length=200)
    votes = models.IntegerField(_("Votos"), default=0)

    class Meta:
        verbose_name = _("Opção")
        verbose_name_plural = _("Opções")

    def __str__(self):
        return f"{self.choice_text}"


