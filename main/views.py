from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "home.html"


class ContactPage(TemplateView):
    template_name = "contact.html"
