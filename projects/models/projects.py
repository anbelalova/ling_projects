from sqlite3 import DatabaseError
from django.db import models
from django.urls import reverse
from .search_model import *

class Projects(models.Model):
	"""Проекты"""
	title = models.CharField('Название_проекта', max_length = 150)
	group = models.ForeignKey('ProjectGroups', verbose_name="Группа", on_delete=models.SET_NULL, null=True)
	language = models.ManyToManyField('ProjectLanguages',blank = True)
	members = models.ManyToManyField('ProjectMembers', blank = True)
	description = models.TextField("Описание", default='')
	short_description = models.TextField("Краткое_описание", default='')
	publications = models.ManyToManyField('ProjectPublications', blank = True)
	qualification_works = models.ManyToManyField('ProjectQualificationWorks', blank = True)
	search_database = models.OneToOneField('ProjectSearch',on_delete=models.SET_NULL, null=True, blank = True)
	url = models.SlugField(max_length=130, unique=True)

	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse('project_detail', kwargs = {'slug': self.url})
	
	class Meta:
		verbose_name = 'Проект'
		verbose_name_plural = 'Проекты'

class ProjectGroups(models.Model):
	"""Группа, к которой относится проект(пр. Глагол, прилагательное)"""
	name = models.CharField('Группа_проекта', max_length = 100)
	url = models.SlugField(max_length=130, unique=True)

	def __str__(self):
		return self.name
	
	class Meta:
		verbose_name = 'Группа проекта'
		verbose_name_plural = 'Группы проекта'

class ProjectLanguages(models.Model):
	"""Язык проекта"""
	language = models.CharField('Язык_проекта', max_length = 100)
	url = models.SlugField(max_length=130, unique=True)

	def __str__(self):
		return self.language
	
	class Meta:
		verbose_name = 'Язык проекта'
		verbose_name_plural = 'Языки проекта'

class ProjectMembers(models.Model):
	"""Участники проекта"""
	fio = models.CharField('ФИО_участника', max_length = 150)
	project_position = models.CharField('Должность_в_проекте', max_length = 150, blank = True)
	link_on_member = models.CharField('Ссылка_на_основную_страницу', max_length = 150, blank = True)

	def __str__(self):
		return self.fio
	
	class Meta:
		verbose_name = 'Участник проекта'
		verbose_name_plural = 'Участники проекта'

class ProjectPublications(models.Model):
	"""Публикации проекта"""
	title = models.CharField('Название_публикации', max_length = 150)
	members = models.ManyToManyField('ProjectMembers', blank = True)
	description = models.TextField("Описание_публикации", default='')
	information = models.TextField("Информация_о_публикации", default='')
	languages = models.ManyToManyField('ProjectLanguages', blank = True)
	year = models.PositiveSmallIntegerField("Дата_публикации", blank = True)
	work_file = models.FileField(upload_to = 'publications/', blank = True)
	url = models.SlugField(max_length=130, unique=True)

	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse('publication', kwargs = {'slug': self.url})
	
	class Meta:
		verbose_name = 'Публикация проекта'
		verbose_name_plural = 'Публикации проекта'

class ProjectQualificationWorks(models.Model):
	"""Квалификационные работы проекта"""
	title = models.CharField('Название_работы', max_length = 150)
	degree = models.CharField('Научная_степень', max_length = 150, blank = True)
	author = models.ManyToManyField('ProjectMembers', blank = True)
	university = models.CharField('Университет_защиты', max_length = 150, blank = True)
	year = models.PositiveSmallIntegerField("Дата_публикации", blank = True)
	work_file = models.FileField(upload_to = 'qualific_works/',blank = True)

	def __str__(self):
		return self.title
	
	class Meta:
		verbose_name = 'Квалификационная работа проекта'
		verbose_name_plural = 'Квалификационные работы проекта'

class ProjectQuestionnaires(models.Model):
	"""Анкеты проекта"""
	title = models.CharField('Название_анкеты', max_length = 150)
	work_file = models.FileField(upload_to = 'questionnaires/', blank = True)
	project = models.ForeignKey('Projects',  on_delete=models.SET_NULL, null=True, blank = True)

	def __str__(self):
		return self.title
	
	class Meta:
		verbose_name = 'Анкета проекта'
		verbose_name_plural = 'Анкеты проекта'