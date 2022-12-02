from django.db import models

class Bb(models.Model):
  title = models.CharField(max_length=50, verbose_name='Товар')
  content = models.TextField(null=True, blank=True, verbose_name='Описание')
  price = models.FloatField(null=True, blank=True, verbose_name='Цена')
  published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
  
  class Meta:
    verbose_name_plural = 'Объявления'
    verbose_name = 'Объявление'
    ordering = ['-published']

class Rubric(models.Model):
  name = models.CharField(max_length=20, db_index=True,  verbose_name='Название')
  def __str__(self):
    return self.name
  class Meta:
    verbose_name_plural = 'Рубрики'
    verbose_name = 'Рубрика'
    ordering = ['name']


class Collection(models.Model):
  name = models.CharField(max_length=50, verbose_name='Название')
  content = models.TextField(null=True, blank=True, verbose_name='Краткое описание')
  start_date= models.DateTimeField(null=True,verbose_name='Период показа')
  fin_date= models.DateTimeField(null=True,verbose_name='Период показа')
  zal= models.ForeignKey('Zal', null=True,   on_delete=models.PROTECT, verbose_name='Выставочный зал')
  
  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name_plural = 'Коллекции'
    verbose_name = 'Коллекция'
    ordering = ['name']

class Exponat(models.Model):
  name = models.CharField(max_length=50, verbose_name='Название')
  content = models.TextField(null=True, blank=True, verbose_name='Краткое описание')
  stoimost = models.FloatField(null=True, blank=True, verbose_name='Страховая стоимость')
  vek_sozdania = models.FloatField(null=True, blank=True, verbose_name='Век создания')
  visota = models.FloatField(null=True, blank=True, verbose_name='Высота')
  shirina = models.FloatField(null=True, blank=True, verbose_name='Ширина')
  dlina = models.FloatField(null=True, blank=True, verbose_name='Длина')
  collection = models.ForeignKey('Collection', null=True,   on_delete=models.PROTECT, verbose_name='Коллекция')
  price = models.FloatField(null=True, blank=True, verbose_name='Цена')
  
  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name_plural = 'Экспонаты'
    verbose_name = 'Экспонат'
    ordering = ['name']

class Zal(models.Model):
  name = models.CharField(max_length=50, verbose_name='Название')
  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name_plural = 'Выставочные залы'
    verbose_name = 'Выставочный зал'
    ordering = ['name']