from django.shortcuts import render,redirect
from django.views import View
from main.aydin.models import *
from django.shortcuts import get_object_or_404
from main.core.utils import get_query,paginate

class BlogView(View):
    template_name= "web/pages/blog-en.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        bloglist = Blog.objects.all()
        bloglist = paginate(objects=bloglist, per_page=6, page=request.GET.get("page"))
        #meta = self.get_object().as_meta(self.request)
        blog_ic = BlogSeoENPageModel.objects.first()
        if request.LANGUAGE_CODE == 'tr' :
            return redirect('web:blog_view')

        self.ctx = {
            'bloglist' : bloglist,
        }
        print(bloglist)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        bloglist = Blog.objects.all()
        title = request.POST.get("title" , None)
        body =  request.POST.get("body",  None)
        image = request.FILES.get("image", None)
        self.ctx = {
            'blogs ' : blogs,
             'blog_ic':blog_ic,

        }
        return render(request, self.template_name, self.ctx)


class BlogDetail(View):
    template_name = "web/pages/blog-detail.html"
    ctx = {}

    def get(self, request, *args, **kwargs):
        blog_id = request.resolver_match.kwargs.get('slug')
        blog = get_object_or_404(Blog, slug=blog_id)
        if request.LANGUAGE_CODE == 'tr' :
            return redirect('/')

        self.ctx = {
            'blog' : blog,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)

class BlogTrView(View):
    template_name= "web/pages/blog-tr.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        bloglist_tr = BlogTr.objects.all()
        bloglist_tr = paginate(objects=bloglist_tr, per_page=6, page=request.GET.get("page"))
        blog_ic = BlogSeoPageModel.objects.first()

        self.ctx = {
            'bloglist_tr' : bloglist_tr,
            'blog_ic':blog_ic,
        }                                                                                                                                                                                                                            
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)


class BlogTrDetail(View):
    template_name = "web/pages/blog-detail-tr.html"
    ctx = {}

    def get(self, request, *args, **kwargs):
        blog_tr_id = request.resolver_match.kwargs.get('slug')
        blogtr = get_object_or_404(BlogTr, slug=blog_tr_id)
        self.ctx = {
            'blogtr' : blogtr,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
    





class KvKKView(View):
    template_name= "web/pages/kvkk.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        kvkk = Kvkk.objects.first()
        if request.LANGUAGE_CODE == 'en' :
            return redirect('web:aydinlatma_metni_en')
        self.ctx = {
            'kvkk' : kvkk,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)


class KvKKENView(View):
    template_name= "web/pages/kvkken.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        kvkk = KvkkEN.objects.first()
        if request.LANGUAGE_CODE == 'tr' :
            return redirect('web:aydinlatma_metni')
        self.ctx = {
            'kvkk' : kvkk,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)