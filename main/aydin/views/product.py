from django.shortcuts import render,redirect
from django.views import View
from main.aydin.models import *
from django.shortcuts import get_object_or_404
from main.core.utils import get_query, paginate


class ProductView(View):
    template_name= "web/pages/product.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        protrlisten = Products.objects.all()
        protrlisten = paginate(objects=protrlisten, per_page=12, page=request.GET.get("page"))
        self.ctx = {
            'protrlisten':protrlisten,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductDetailENView(View):
    template_name= "web/pages/product-en-detail.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        ster_tr_id = request.resolver_match.kwargs.get('slug')
        pro = get_object_or_404(Products, slug=ster_tr_id)
        products = Products.objects.all().exclude(title=pro)

        if request.LANGUAGE_CODE == 'tr' :
            return redirect('/')
        self.ctx = {
            'pro' : pro,
            'products' : products,

        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
    

class ProductTrView(View):
    template_name= "web/pages/product-tr.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        protrlist = ProductsTr.objects.all()
        count = ProductsTr.objects.all().count()
        protrlist = paginate(objects=protrlist, per_page=12, page=request.GET.get("page"))

        self.ctx = {
            'count' : count,
            'protrlist':protrlist,
        }
        return render(request, self.template_name, self.ctx)
    
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
    
class ProductDetailTrView(View):
    template_name= "web/pages/product-tr-detail.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        ster_tr_id = request.resolver_match.kwargs.get('slug')
        pro = get_object_or_404(ProductsTr, slug=ster_tr_id)


        products = ProductsTr.objects.all().exclude(title=pro)
        self.ctx = {
            'pro' : pro,
            'products' : products,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
    
class ProductCategoryTrView(View):
    template_name= "web/pages/product-cat-tr.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        categories = ProductCategoryTR.objects.all()
        self.ctx = {
            'categories' : categories,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
    

class ProductCategoryDetailTrView(View):
    template_name= "web/pages/product-cat-tr-detail.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        ster_tr_id = request.resolver_match.kwargs.get('id')
        category = ProductCategoryTR.objects.filter(id=ster_tr_id).first()

        products = ProductsTr.objects.filter(subcategory__id=ster_tr_id)
        self.ctx = {
            "category" : category,
            'protrlist' : products,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
    
class ProductTrDISBView(View):
    template_name= "web/pages/dis.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        dis = ProductsTr.objects.filter(category=ProductsTr.DIS)
        #dıs = paginate(objects=dıs, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'dis':dis,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)

class ProductTrICBView(View):
    template_name= "web/pages/ic.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        ic = ProductsTr.objects.filter(category=ProductsTr.IC)
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'ic':ic,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductTrYRDBView(View):
    template_name= "web/pages/yrd.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        yrd = ProductsTr.objects.filter(category=ProductsTr.YRD)
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'yrd':yrd,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductTrCaddBView(View):
    template_name= "web/pages/products/caddeay.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        pro = ProductsTr.objects.filter(subcategory__name="Cadde Aydınlatması")
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'pro':pro,
        }
        print(pro)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductTrLineerLedView(View):
    template_name= "web/pages/products/linnerled.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        pro = ProductsTr.objects.filter(subcategory__name="Lineer LedTube Volans")
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'pro':pro,
        }
        print(pro)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductTrDotLedView(View):
    template_name= "web/pages/products/dotled.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        pro = ProductsTr.objects.filter(subcategory__name="Dot Led Scorpius")
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'pro':pro,
        }
        print(pro)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductTrProjectorView(View):
    template_name= "web/pages/products/projector.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        pro = ProductsTr.objects.filter(subcategory__name="Projector")
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'pro':pro,
        }
        print(pro)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductTrElfeView(View):
    template_name= "web/pages/products/elfe.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        pro = ProductsTr.objects.filter(subcategory__name="El Feneri")
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'pro':pro,
        }
        print(pro)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductTrParkView(View):
    template_name= "web/pages/products/park.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        pro = ProductsTr.objects.filter(subcategory__name="Park Bahçe Aydınlatması")
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'pro':pro,
        }
        print(pro)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductTrWallwasherView(View):
    template_name= "web/pages/products/wall.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        pro = ProductsTr.objects.filter(subcategory__name="Wallwasher")
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'pro':pro,
        }
        print(pro)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductTrMobisView(View):
    template_name= "web/pages/products/mobis.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        pro = ProductsTr.objects.filter(subcategory__name="Mobil Işık Kulesi")
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'pro':pro,
        }
        print(pro)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductTrAracUstuView(View):
    template_name= "web/pages/products/aracustu.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        pro = ProductsTr.objects.filter(subcategory__name="Araç Üstü Işık Kulesi")
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'pro':pro,
        }
        print(pro)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductTrAksesuarlarView(View):
    template_name= "web/pages/products/aksesuarlar.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        pro = ProductsTr.objects.filter(subcategory__name="Aksesuarlar")
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'pro':pro,
        }
        print(pro)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductTrPorTatifUFLEDView(View):
    template_name= "web/pages/products/portufled.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        pro = ProductsTr.objects.filter(subcategory__name="Portatif Alan Aydınlatması UFLED")
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'pro':pro,
        }
        print(pro)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductTrYBTsedView(View):
    template_name= "web/pages/products/ybtsed.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        pro = ProductsTr.objects.filter(subcategory__name="Modüler Led Aydınlatma Seti YBT")
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'pro':pro,
        }
        print(pro)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductTrDekredampulView(View):
    template_name= "web/pages/products/dekredampdis.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        pro = ProductsTr.objects.filter(subcategory__name="Dekoratif Led Ampül").filter(category=ProductsTr.DIS)
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'pro':pro,
        }
        print(pro)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductTrDekredampulIcView(View):
    template_name= "web/pages/products/dekredampic.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        pro = ProductsTr.objects.filter(subcategory__name="Dekoratif Led Ampül").filter(category=ProductsTr.IC)
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'pro':pro,
        }
        print(pro)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductTrYuksekTavansedView(View):
    template_name= "web/pages/products/yuksektavan.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        pro = ProductsTr.objects.filter(subcategory__name="Yüksek Tavan Led Aydınlatması")
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'pro':pro,
        }
        print(pro)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)

class ProductTrDekoratifLedView(View):
    template_name= "web/pages/products/dekledset.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        pro = ProductsTr.objects.filter(subcategory__name="Dekoratif Led Aydınlatma Seti")
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'pro':pro,
        }
        print(pro)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
        
class ProductTrCobledView(View):
    template_name= "web/pages/products/cobled.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        pro = ProductsTr.objects.filter(subcategory__name="COB LED Modül Armekeddon")
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'pro':pro,
        }
        print(pro)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
        
class ProductTrVaterProfConView(View):
    template_name= "web/pages/products/waterprof.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        pro = ProductsTr.objects.filter(subcategory__name="Waterproof Konnektörler")
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'pro':pro,
        }
        print(pro)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
        
class ProductTrVaterProfEnerView(View):
    template_name= "web/pages/products/waterprofener.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        pro = ProductsTr.objects.filter(subcategory__name="Waterproof Enerji Dağıtıcı")
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'pro':pro,
        }
        print(pro)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
        














class ProductDISBView(View):
    template_name= "web/pages/disin.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        dis = Products.objects.filter(category=Products.DIS)
        #dıs = paginate(objects=dıs, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'dis':dis,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)

class ProductICBView(View):
    template_name= "web/pages/icin.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        ic = Products.objects.filter(category=Products.IC)
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'ic':ic,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductYRDBView(View):
    template_name= "web/pages/yrdin.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        yrd = Products.objects.filter(category=Products.YRD)
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'yrd':yrd,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductCaddBView(View):
    template_name= "web/pages/productsen/caddeay.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        pro = Products.objects.filter(subcategory__name="Cadde Aydınlatması")
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'pro':pro,
        }
        print(pro)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductLineerLedView(View):
    template_name= "web/pages/productsen/linnerled.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        pro = Products.objects.filter(subcategory__name="Lineer LedTube Volans")
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'pro':pro,
        }
        print(pro)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductDotLedView(View):
    template_name= "web/pages/productsen/dotled.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        pro = Products.objects.filter(subcategory__name="Dot Led Scorpius")
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'pro':pro,
        }
        print(pro)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductProjectorView(View):
    template_name= "web/pages/productsen/projector.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        pro = Products.objects.filter(subcategory__name="Projector")
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'pro':pro,
        }
        print(pro)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductElfeView(View):
    template_name= "web/pages/productsen/elfe.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        pro = Products.objects.filter(subcategory__name="El Feneri")
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'pro':pro,
        }
        print(pro)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductParkView(View):
    template_name= "web/pages/productsen/park.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        pro = Products.objects.filter(subcategory__name="Park Bahçe Aydınlatması")
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'pro':pro,
        }
        print(pro)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductWallwasherView(View):
    template_name= "web/pages/productsen/wall.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        pro = Products.objects.filter(subcategory__name="Wallwasher")
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'pro':pro,
        }
        print(pro)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductMobisView(View):
    template_name= "web/pages/productsen/mobis.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        pro = Products.objects.filter(subcategory__name="Mobil Işık Kulesi")
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'pro':pro,
        }
        print(pro)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductAracUstuView(View):
    template_name= "web/pages/productsen/aracustu.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        pro = Products.objects.filter(subcategory__name="Araç Üstü Işık Kulesi")
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'pro':pro,
        }
        print(pro)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductAksesuarlarView(View):
    template_name= "web/pages/productsen/aksesuarlar.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        pro = Products.objects.filter(subcategory__name="Aksesuarlar")
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'pro':pro,
        }
        print(pro)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductPorTatifUFLEDView(View):
    template_name= "web/pages/productsen/portufled.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        pro = Products.objects.filter(subcategory__name="Portatif Alan Aydınlatması UFLED")
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'pro':pro,
        }
        print(pro)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductYBTsedView(View):
    template_name= "web/pages/productsen/ybtsed.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        pro = Products.objects.filter(subcategory__name="Modüler Led Aydınlatma Seti YBT")
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'pro':pro,
        }
        print(pro)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductDekredampulView(View):
    template_name= "web/pages/productsen/dekredampdis.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        pro = Products.objects.filter(subcategory__name="Dekoratif Led Ampül").filter(category=Products.DIS)
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'pro':pro,
        }
        print(pro)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductDekredampulIcView(View):
    template_name= "web/pages/productsen/dekredampic.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        pro = Products.objects.filter(subcategory__name="Dekoratif Led Ampül").filter(category=Products.IC)
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'pro':pro,
        }
        print(pro)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductYuksekTavansedView(View):
    template_name= "web/pages/productsen/yuksektavan.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        pro = Products.objects.filter(subcategory__name="Yüksek Tavan Led Aydınlatması")
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'pro':pro,
        }
        print(pro)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)

class ProductDekoratifLedView(View):
    template_name= "web/pages/productsen/dekledset.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        pro = Products.objects.filter(subcategory__name="Dekoratif Led Aydınlatma Seti")
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'pro':pro,
        }
        print(pro)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
        
class ProductCobledView(View):
    template_name= "web/pages/productsen/cobled.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        pro = Products.objects.filter(subcategory__name="COB LED Modül Armekeddon")
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'pro':pro,
        }
        print(pro)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
        
class ProductVaterProfConView(View):
    template_name= "web/pages/productsen/waterprof.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        pro = Products.objects.filter(subcategory__name="Waterproof Konnektörler")
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'pro':pro,
        }
        print(pro)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
        
class ProductVaterProfEnerView(View):
    template_name= "web/pages/productsen/waterprofener.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        pro = Products.objects.filter(subcategory__name="Waterproof Enerji Dağıtıcı")
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        #if request.LANGUAGE_CODE == 'en' :
        #    return redirect('web:mccben')

        self.ctx = {
            'pro':pro,
        }
        print(pro)
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
        
