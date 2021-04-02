from django.contrib import admin
from .models import Definition, DefinitionsForTerm, Explanation, ExplanationLinks, Videos

admin.site.register(Definition)
admin.site.register(DefinitionsForTerm)
admin.site.register(Explanation)
admin.site.register(ExplanationLinks)
admin.site.register(Videos)


