from django.db import models

class Bb(models.Model):
  title = models.CharField(max_length=50, verbose_name='Товар')
  content = models.TextField(null=True, blank=True, verbose_name='Описание')
  price = models.FloatField(null=True, blank=True, verbose_name='Цена')
  published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
  
  class Meta:
    verbose_name_plural = 'Выставочные залы'
    verbose_name = 'Выставочные залы'
    ordering = ['-published']

class Rubric(models.Model):
  name = models.CharField(max_length=20, db_index=True,
  verbose_name='Название')
  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name_plural = 'Коллекции'
    verbose_name = 'Коллекции'
    ordering = ['name']

class Meta:
    verbose_name_plural = 'Экспонаты'
    verbose_name = 'Экспонаты'
    ordering = ['name1']