#definimos todos os objetos chamados Modelos

from django.db import models
from django.utils import timezone

#A linha abaixo define o nosso modelo (� um objeto).
#models.Model significa que o Montar � um modelo de Django, ent�o o Django sabe que ele deve ser salvo no banco de dados.
class Grade(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #Este � um link para outro modelo.
    title = models.CharField(max_length=200) #� assim que definimos um texto com um n�mero limitado de caracteres.
    text = models.TextField() #Este campo � para textos sem um limite fixo
    created_date = models.DateTimeField( #Este � uma data e hora.
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def montar(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# Create your models here.
