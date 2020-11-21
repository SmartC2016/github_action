# pages/views.py

from django.views.generic import TemplateView


class StartPage(TemplateView):
    template_name = 'pages/home.html'
