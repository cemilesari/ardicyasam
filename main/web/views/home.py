# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from django.utils import timezone as djtz
from django.conf import settings

from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages

from django.template.loader import render_to_string
from main.aydin.models import *
from main.core.utils import get_query, paginate

class HomeView(View):
    template_name = "web/welcome.html"
    ctx = {}
    def get(self, request, *args, **kwargs):

        slidertr = Slider.objects.all()[:1].first()
        slidertriki = Slider.objects.all()[1:2].first()
        slidertruc = Slider.objects.all()[2:3].first()

        slideren = SliderEN.objects.all()
        cont = HomeSeo.objects.first()
        bloglist_tr = BlogTr.objects.all()[:3]
        bloglist = Blog.objects.all()[:3]
        about = AboutTR.objects.first()

        proj = ProjectsTR.objects.all()
        projen = Projects.objects.all()
        protrlist = ProductsTr.objects.all()
        protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        categories = ProductCategoryTR.objects.all().order_by('ordering')
        cat3 = ProductCategoryTR.objects.all()[:3]


        self.ctx ={
            'cont':cont,
            'first' : slidertr,
            "second" : slidertriki,
            "third" : slidertruc,
            'slideren' : slideren,
            'bloglist_tr':bloglist_tr,
            'proj' : proj,
            'projen':projen,
            'bloglist':bloglist,
            "about" : about,
            "protrlist" : protrlist,
            "categories" : categories,
            "cat3" : cat3,

        }
        return render(request, self.template_name,self.ctx)
    def post(self,request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)

def global_manage(request):
    args, resstatus, resmessage = {}, 400, ("Sorry, Command does not matched.")
    if request.GET and request.is_ajax():
        s = request.GET.get("s")
    if isinstance(args, dict):
        args["status"] = resstatus
        args["message"] = str(resmessage)
    else:
        resstatus = 200
    return HttpResponse(json.dumps(args), status=resstatus, content_type="application/json")



class NewView(View):
    template_name = "web/new.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,self.ctx)
    def post(self,request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
 