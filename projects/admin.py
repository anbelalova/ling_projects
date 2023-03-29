from django.contrib import admin
from .models import Projects, ProjectGroups, ProjectLanguages, ProjectMembers, ProjectPublications, ProjectQualificationWorks, ProjectQuestionnaires, ProjectSearch, SearchObjects, SearchLanguages, FirstLevelFrames, SecondLevelFrames, Metaphors, Examples

admin.site.register(Projects)
admin.site.register(ProjectGroups)
admin.site.register(ProjectLanguages)
admin.site.register(ProjectMembers)
admin.site.register(ProjectPublications)
admin.site.register(ProjectQualificationWorks)
admin.site.register(ProjectQuestionnaires)
admin.site.register(ProjectSearch)
admin.site.register(SearchObjects)
admin.site.register(SearchLanguages)
admin.site.register(FirstLevelFrames)
admin.site.register(SecondLevelFrames)
admin.site.register(Metaphors)
admin.site.register(Examples)
