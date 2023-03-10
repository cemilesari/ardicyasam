from django.shortcuts import render,redirect
from django.views import View
from django.shortcuts import get_object_or_404
from main.core.utils import get_query,paginate
from main.aydin.models import *


class AboutView(View):
    template_name= "web/pages/about.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        about = About.objects.first()
        if request.LANGUAGE_CODE == 'tr' :
            return redirect('web:about')
        self.ctx = {
            'about' : about,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)


class AboutTRView(View):
    template_name= "web/pages/about_tr.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        about = AboutTR.objects.first()
        self.ctx = {
            'about' : about,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)

