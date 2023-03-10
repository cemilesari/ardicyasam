from django.shortcuts import render,redirect
from django.views import View
from django.core.mail import EmailMultiAlternatives
from main.aydin.forms import SupportForm
from main.aydin.models import *
from django.contrib import messages
from django.utils.html import strip_tags

from django.template.loader import render_to_string
class BecomeSupport(View):
    template_name = "web/pages/contact.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        cont = İletisimSeo.objects.first()
        if request.LANGUAGE_CODE == 'tr' :
            return redirect('web:contact')
        self.ctx ={
            'cont':cont,
        }
        return render(request, self.template_name,self.ctx)
    def post(self,request, *args, **kwargs):
        form = SupportForm()
        full_name = request.POST.get("full_name",None)
        email         = request.POST.get("email", None)
        body           = request.POST.get("body", None)
        tel           = request.POST.get("tel", None)

        form.is_valid()
        obj = Support.objects.create(
            full_name = full_name or "Untitled Partner Name",
            email = email,
            body = body,
            tel = tel,
        )
        obj.save()

        resstatus, resmessage = 200, ("Your contact request has been created successfully. ")
        if resstatus == 200:
            messages.success(request, ("Your contact request has been created successfully."))
        self.ctx = {
            'full_name' : full_name,
            'email'         : email,
            'body'           : body,
            'tel'       : tel,
        }
        return render(request, self.template_name, self.ctx)

class IletisimSup(View):
    template_name = "web/pages/iletisim.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        cont = İletisimSeoTR.objects.first()

        self.ctx ={
            'cont':cont,
        }
        return render(request, self.template_name,self.ctx)
    def post(self,request, *args, **kwargs):
        form = SupportForm()
        full_name = request.POST.get("full_name",None)
        email         = request.POST.get("email", None)
        body           = request.POST.get("body", None)
        tel           = request.POST.get("tel", None)

        form.is_valid()
        obj = Support.objects.create(
            full_name = full_name or "Untitled Partner Name",
            email = email,
            body = body,
            tel = tel,
        )
        obj.save()
        resstatus, resmessage = 200, ("İletişim Taleniniz alındı.")
        if resstatus == 200:
            messages.success(request, ("İletişim Taleniniz alındı."))

        self.ctx = {
            'full_name' : full_name,
            'email'         : email,
            'body'           : body,
            'tel'       : tel,
        }
        return render(request, self.template_name, self.ctx)