from django.db import models
from django.urls import reverse

class ProjectSearch(models.Model):
	title = models.CharField('Название_бд', max_length = 150)
	url = models.SlugField(max_length=130, unique=True)

	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse('questionnaire', kwargs = {'slug': self.url})

	class Meta:
		verbose_name = 'БД проекта'
		verbose_name_plural = 'БД проектов'

class SearchObjects(models.Model):
	project = models.ForeignKey('ProjectSearch',  on_delete=models.SET_NULL, null=True, blank = True)
	word = models.CharField(max_length=150, verbose_name = 'Слово')
	translation = models.CharField(max_length=150, verbose_name = 'Перевод')
	language = models.ForeignKey('SearchLanguages',  on_delete=models.SET_NULL, null=True, blank = True)
	frame = models.ForeignKey('SecondLevelFrames',  on_delete=models.SET_NULL, null=True, blank = True)
	construction_is = models.BooleanField(default = True, blank = True)
	construction = models.CharField(max_length=150, null=True, blank = True, verbose_name = 'Конструкция')
	comment = models.TextField(null=True, blank = True)

	def __str__(self):
		return self.word

	class Meta:
		verbose_name = 'Слово'
		verbose_name_plural = 'Слова'

class SearchLanguages(models.Model):
	language = models.CharField(max_length=150, verbose_name = 'Язык')
	author = models.CharField(max_length=150, verbose_name = 'Сборщик данных', blank = True)
	project = models.ForeignKey('ProjectSearch',  on_delete=models.SET_NULL, null=True, blank = True)

	def __str__(self):
		return self.language

	class Meta:
		verbose_name = 'Язык'
		verbose_name_plural = 'Языки'

class FirstLevelFrames(models.Model):
	frame = models.CharField(max_length=150, verbose_name = 'Фрейм')
	project = models.ForeignKey('ProjectSearch',  on_delete=models.SET_NULL, null=True, blank = True)

	def __str__(self):
		return self.frame

	class Meta:
		verbose_name = 'Фрейм 1 уровня'
		verbose_name_plural = 'Фреймы 1 уровня'

class SecondLevelFrames(models.Model):	
	parent_frame = models.ForeignKey('FirstLevelFrames', on_delete=models.SET_NULL, null=True, blank = True, verbose_name='Родительский фрейм')
	second_frame = models.CharField(max_length=150, verbose_name = 'Фрейм')
	video_is = models.BooleanField(default = False, blank = True)
	image_is = models.BooleanField(default = False, blank = True)
	frame_image = models.FileField(upload_to = 'images/',verbose_name='Изображение', blank = True)

	def __str__(self):
		return self.second_frame

	class Meta:
		verbose_name = 'Фрейм 2 уровня'
		verbose_name_plural = 'Фреймы 2 уровня'

class Metaphors(models.Model):
	word = models.ForeignKey('SearchObjects',  on_delete=models.SET_NULL, null=True, blank = True)
	metaphor = models.CharField(max_length=150, verbose_name = 'Метафора', null=True, blank = True)
	ex_metaphor = models.CharField(max_length=150, verbose_name = 'Пример метафоры')
	metaphor_translation = models.CharField(max_length=150, verbose_name = 'Перевод метафоры')

	def __str__(self):
		return self.metaphor

	class Meta:
		verbose_name = 'Метафора'
		verbose_name_plural = 'Метафоры'

class Examples(models.Model):
	word = models.ForeignKey('SearchObjects',  on_delete=models.SET_NULL, null=True, blank = True)
	eg = models.CharField(max_length=150, verbose_name = 'Пример использования')
	eg_translation = models.CharField(max_length=150, verbose_name = 'Перевод примера')

	def __str__(self):
		return self.eg

	class Meta:
		verbose_name = 'Пример использования'
		verbose_name_plural = 'Примеры использования'