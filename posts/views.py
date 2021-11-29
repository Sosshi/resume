from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Experience, Skill, Education


class WorksPage(TemplateView):
    template_name = "works.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["education"] = Education.objects.all
        context["experiences"] = Experience.objects.all
        context["skills"] = Skill.objects.all
        return context
