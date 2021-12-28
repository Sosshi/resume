from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth import get_user_model


class HomePage(TemplateView):
    template_name = "home.html"


class ContactPage(TemplateView):
    template_name = "contact.html"


class Aboutpage(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = get_user_model().objects.get(pk=1)
        return context


def contact(request):
    email = request.POST.get("email")
    subject = request.POST.get("subject")
    message = request.POST.get("message")
    if email and subject and message:
        try:
            send_mail(
                subject=subject,
                message=message,
                from_email="davie@gmail.com",
                recipient_list=[email],
            )
            return HttpResponse("Message Sent")
        except Exception as e:
            return HttpResponse(f"Message Not Sent {e}")
    else:
        return HttpResponse("Cannot sent empty mail")
