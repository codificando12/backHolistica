from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

# Create your models here.

class Terapia(models.Model):
    name = models.CharField(max_length=255, verbose_name='name')
    description = models.TextField(verbose_name='description')

    class Meta:
        verbose_name = 'terapia'
        verbose_name_plural = 'terapias'

    def __str__(self):
        return self.name
    

class Terapeutas(models.Model):
    owner = models.ForeignKey('auth.User', related_name='terapeutas', on_delete=models.CASCADE)
    highlighted = models.TextField()

    register = models.TimeField(auto_now_add=True)
    name= models.CharField(max_length=255, verbose_name='name')
    last_name = models.CharField(max_length=255, verbose_name='last_name')
    description = models.TextField(verbose_name='description')
    terapias = models.ForeignKey(Terapia, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'terapeuta'
        verbose_name_plural = 'terapeutas'
        ordering = ['id']


    # Revisar esto
    # def save(self, *args, **kwargs):
    #     """
    #     Use the `pygments` library to create a highlighted HTML
    #     representation of the code snippet.
    #     """
    #     lexer = get_lexer_by_name(self.language)
    #     linenos = 'table' if self.linenos else False
    #     options = {'title': self.title} if self.title else {}
    #     formatter = HtmlFormatter(style=self.style, linenos=linenos, full=True, **options)
    #     self.highlighted = highlight(self.code, lexer, formatter)

    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.name