from django.db import models


class Luz(models.Model):
    luz = models.CharField('Luz Necessária', max_length=45)

    def __str__(self):
        return self.luz

    class Meta:
        db_table = 'luzes'
        verbose_name_plural = "luzes"


class Produto(models.Model):
    produto = models.CharField(unique=True, max_length=45, blank=False)
    valor = models.DecimalField(max_digits=11, decimal_places=2, blank=False)
    url_imagem = models.CharField(max_length=255, blank=True)
    tamanho_pote = models.IntegerField('Tamanho do Pote (cm)', blank=False)
    rega_necessaria = models.IntegerField('Rega Necessária (x por semana)', blank=False)
    id_luz = models.ForeignKey(Luz, models.RESTRICT, db_column='id_luz', null=False, verbose_name='Luz Necessária')
    toxica_animais = models.BooleanField('Tóxica para Animais?')

    def __str__(self):
        return self.produto

    class Meta:
        db_table = 'produtos'
        verbose_name_plural = "produtos"
