from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View


from .models import Projects, ProjectPublications, SearchObjects, SearchLanguages, FirstLevelFrames, SecondLevelFrames, ProjectSearch, Metaphors

class ProjectsView(ListView):
	"""Представление списка проектов"""

	model = Projects
	queryset = Projects.objects.all()

class ProjectDetailView(DetailView):
	"""Представление одного проекта"""

	model = Projects
	slug_field = 'url'


class PublicationView(View):
	"""Представление публикации проекта"""
	def get(self, request, slug):
		publication = ProjectPublications.objects.get(url = slug)
		return render(request, 'projects/publication.html', {'publication': publication} )

class QuestionnaireView(View):
	"""Представление анкеты для поиска"""

	def get(self, request, slug):
		searchobject = ProjectSearch.objects.get(url = slug)
		words = SearchObjects.objects.all()
		slanguage = SearchLanguages.objects.all()
		fframe = FirstLevelFrames.objects.all()
		sframe = SecondLevelFrames.objects.all()
		context = {
			'words': words, 
			'searchobject': searchobject, 
			'slanguage': slanguage, 
			'fframe':fframe,  
			'sframe':sframe,
		}
		return render(request, 'projects/questionnaire.html', context )

class DBView(ListView):
	"""Представление полной базы данных проекта"""

	def get(self, request, pk):
		searchobject = ProjectSearch.objects.get(id = pk)
		words = SearchObjects.objects.all()
		context = {
			'words': words, 
			'searchobject': searchobject,
		}
		return render(request, 'projects/db_search.html', context )

class Search(ListView):
	"""Осуществление поиска по языку"""

	template_name = 'projects/search.html'
	context_object_name = 'words'
	def get_queryset(self):
		query = self.request.GET.get('q')
		return SearchObjects.objects.filter(language__language=query)
	
	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['q'] = self.request.GET.get('q')
		return context

class Filter(ListView):
	"""Осуществление поиска по фрейму"""

	template_name = 'projects/filter.html'
	context_object_name = 'Words'

	def get_queryset(self):
		query_language = self.request.GET.getlist('language')
		query_frame = self.request.GET.getlist('frame')
		queryset = SearchObjects.objects.filter(language__in=query_language, frame__in = query_frame)
		return queryset
