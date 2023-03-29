from django.urls import path
from . import views

urlpatterns = [
	path('', views.ProjectsView.as_view(), name = 'home'),
	path('project/<slug:slug>/', views.ProjectDetailView.as_view(), name = 'project_detail'),
	path('publication/<slug:slug>/', views.PublicationView.as_view(), name = 'publication'),
	path('questionnaire/<slug:slug>/', views.QuestionnaireView.as_view(), name='questionnaire'),
	path('filter/', views.Filter.as_view(), name='filter'),
	path('db_search/<int:pk>/', views.DBView.as_view(), name='db_search'),
	path('db_search/<int:pk>/search/', views.Search.as_view(), name='search'),
]