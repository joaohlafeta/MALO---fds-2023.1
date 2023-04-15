from django.db import models
from django.core.validators import MinValueValidator



# Create your models here.



class Ingredient(models.Model):
    name = models.CharField('Ingrediente', max_length=120) 
    '''nome do ingrediente'''
    exp_date = models.DateField('Data de validade') 
    '''data de validade'''
    quantity = models.FloatField('Quantidade') 
    '''quantidade que consta no estoque do ingrediente'''
    measure_unit = models.CharField('Unidade de medida',max_length=10) 
    '''unidade de medida utilzada ex.: kg, gramas, etc'''
    price = models.FloatField('Preço de compra(total)')
    '''preco de compra do ingrediente (total)'''
    obs = models.TextField('Observação', blank=True)
    '''ex.: marca parmalate, deixar na geladeira, etc'''

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField('Nome do prato', max_length=120)
    '''Nome do prato'''
    price = models.FloatField('Preço de venda')
    '''Preço do prato'''
    description = models.TextField('Descrição')
    '''Descrição do prato'''
    ingredients = models.ManyToManyField(Ingredient)
    '''Ingredientes utilizados no prato'''

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField('Categoria', max_length=120)
    '''Nome da categoria'''
    dishes = models.ManyToManyField(Dish, blank=True)
    '''Pratos na categoria'''

    def __str__(self):
        return self.name  

class Mesa(models.Model):
    numero = models.IntegerField(unique=True)
    descricao = models.CharField(max_length=100, default='Mesa')

    @classmethod
    def proximo_numero(cls):
        ultima_mesa = cls.objects.order_by('-numero').first()
        numero = ultima_mesa.numero + 1 if ultima_mesa else 1
        return numero

    def __str__(self):
        return f'Mesa {self.numero}'

    