from django.shortcuts import render,redirect
from django.views import View
from main.aydin.models import *
from django.shortcuts import get_object_or_404
from main.core.utils import get_query, paginate


class ProjectsTRView(View):
    template_name= "web/pages/projects.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        proj = ProjectsTR.objects.all()
        proj = paginate(objects=proj, per_page=12, page=request.GET.get("page"))
        categ = CategoryTR.objects.all()
        blog_ic = ProjectsTRSeoTR.objects.first()


        self.ctx = {
            'proj':proj,
            'categ' : categ,
            'blog_ic':blog_ic,
        }
        
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProjectsView(View):
    template_name= "web/pages/projects.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        proj = Projects.objects.all()
        proj = paginate(objects=proj, per_page=12, page=request.GET.get("page"))
        blog_ic = ProjectsSeoTR.objects.first()

        categ = CategoryTR.objects.all()
        if request.LANGUAGE_CODE == 'tr' :
            return redirect('web:project')

        self.ctx = {
            'proj':proj,
            'categ' : categ,
            'blog_ic':blog_ic,

        }
        
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)

class ProjectsDetailTrView(View):
    template_name= "web/pages/projects-tr-detail.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        ster_tr_id = request.resolver_match.kwargs.get('slug')
        pro = get_object_or_404(ProjectsTR, slug=ster_tr_id)
        if request.LANGUAGE_CODE == 'en' :
            return redirect('/')
        self.ctx = {
            'pro' : pro,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)

class ProjectsDetailENView(View):
    template_name= "web/pages/projects-en-detail.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        ster_tr_id = request.resolver_match.kwargs.get('slug')
        pro = get_object_or_404(Projects, slug=ster_tr_id)
        if request.LANGUAGE_CODE == 'tr' :
            return redirect('/')
        self.ctx = {
            'pro' : pro,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)


class ProjectsSportTRView(View):
    template_name= "web/pages/projects/sport.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        proj = ProjectsTR.objects.filter(category__name="SPOR TESİSLERİ")
        proj = paginate(objects=proj, per_page=12, page=request.GET.get("page"))
        categ = CategoryTR.objects.all()
        if request.LANGUAGE_CODE == 'en' :
            return redirect('web:sporen')
        self.ctx = {
            'proj':proj,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProjectsGayrTRView(View):
    template_name= "web/pages/projects/gayr.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        proj = ProjectsTR.objects.filter(category__name="GAYRİMENKUL VE İNŞAAT")
        proj = paginate(objects=proj, per_page=12, page=request.GET.get("page"))
        categ = CategoryTR.objects.all()
        if request.LANGUAGE_CODE == 'en' :
            return redirect('web:gayinen')

        self.ctx = {
            'proj':proj,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProjectsHalkTRView(View):
    template_name= "web/pages/projects/halk.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        proj = ProjectsTR.objects.filter(category__name="HALKA AÇIK ALANLAR")
        proj = paginate(objects=proj, per_page=12, page=request.GET.get("page"))
        categ = CategoryTR.objects.all()
        if request.LANGUAGE_CODE == 'en' :
            return redirect('web:halacen')
        self.ctx = {
            'proj':proj,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)

class ProjectsOzkTRView(View):
    template_name= "web/pages/projects/ozk.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        proj = ProjectsTR.objects.filter(category__name="ÖZEL KURUMLAR")
        proj = paginate(objects=proj, per_page=12, page=request.GET.get("page"))
        categ = CategoryTR.objects.all()
        if request.LANGUAGE_CODE == 'en' :
            return redirect('web:ozkuren')
        self.ctx = {
            'proj':proj,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProjectsKamuTRView(View):
    template_name= "web/pages/projects/kam.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        proj = ProjectsTR.objects.filter(category__name="KAMU KURUMLARI")
        proj = paginate(objects=proj, per_page=12, page=request.GET.get("page"))
        categ = CategoryTR.objects.all()
        if request.LANGUAGE_CODE == 'en' :
            return redirect('web:kamuen')
        self.ctx = {
            'proj':proj,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)




class ProjectsSportView(View):
    template_name= "web/pages/projects/sporten.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        proj = Projects.objects.filter(category__name="SPORTS FACILITIES")
        proj = paginate(objects=proj, per_page=12, page=request.GET.get("page"))
        if request.LANGUAGE_CODE == 'tr' :
            return redirect('web:spor')
        self.ctx = {
            'proj':proj,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProjectsGayrView(View):
    template_name= "web/pages/projects/gayren.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        proj = Projects.objects.filter(category__name="REAL ESTATE AND CONSTRUCTION")
        proj = paginate(objects=proj, per_page=12, page=request.GET.get("page"))
        if request.LANGUAGE_CODE == 'tr' :
            return redirect('web:gayin')
        self.ctx = {
            'proj':proj,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProjectsHalkView(View):
    template_name= "web/pages/projects/halken.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        proj = Projects.objects.filter(category__name="PUBLIC AREAS")
        proj = paginate(objects=proj, per_page=12, page=request.GET.get("page"))
        if request.LANGUAGE_CODE == 'tr' :
            return redirect('web:halac')
        self.ctx = {
            'proj':proj,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)

class ProjectsOzkView(View):
    template_name= "web/pages/projects/ozken.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        proj = Projects.objects.filter(category__name="PRIVATE INSTITUTIONS")
        proj = paginate(objects=proj, per_page=12, page=request.GET.get("page"))
        if request.LANGUAGE_CODE == 'tr' :
            return redirect('web:ozkur')
        self.ctx = {
            'proj':proj,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProjectsKamuView(View):
    template_name= "web/pages/projects/kamen.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        proj = Projects.objects.filter(category__name="PUBLIC INSTITUTIONS")
        proj = paginate(objects=proj, per_page=12, page=request.GET.get("page"))
        if request.LANGUAGE_CODE == 'tr' :
            return redirect('web:kamu')
        self.ctx = {
            'proj':proj,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)