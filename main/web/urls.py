# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import gettext_lazy as _
from django.urls import path

from .views import *
from main.aydin.views import *
app_name = 'web'

urlpatterns = [
	path('manage/', global_manage, name='global_manage'),
	path('', HomeView.as_view(), name='welcome_view'),

	path('blog-list/', 				                               view=BlogView.as_view(),                     name='blog_view_en'),
	path('blog-detail/<slug:slug>/' ,                              view=BlogDetail.as_view(),                   name="blog_detail_en"),
	path('blog/', 			    		                           view=BlogTrView.as_view(),                   name='blog_view'),
	path('blog-detay/<slug:slug>/',                                view=BlogTrDetail.as_view(),                 name="blog_detail"),

	path('aydinlatma-metni/',                                      view=KvKKView.as_view(),                     name="aydinlatma_metni"),
	path('privacy-policy/',       		                           view=KvKKENView.as_view(),                   name="aydinlatma_metni_en"),
                        
	path('about/',                                                 view=AboutView.as_view(),                    name='about_en'),
	path('hakkimizda/',                                            view=AboutTRView.as_view(),                  name='about'),
	path('iletisim/',                                              view=IletisimSup.as_view(),                  name='contact'),
	path('contact/',                                               view=BecomeSupport.as_view(),                name='contact_en'),
	path('urun-kategorileri',                               view=ProductCategoryTrView.as_view(),         name='prod-cat'),
	path('ekibimiz',                               view=TeamsView.as_view(),         name='teams'),

	path('urun-kategorileri/<id>/',                               view=ProductCategoryDetailTrView.as_view(),         name='prod-cat-det'),
	path('ekibimiz/<id>/',                               view=TeamsDetailView.as_view(),         name='team-det'),

	path('urunler/',                     		                   view=ProductTrView.as_view(),                name='per_view'),
	path('urun-detay/<slug:slug>/',      		                   view=ProductDetailTrView.as_view(),          name='per_detail_view'),
	path('products/',                    		                   view=ProductView.as_view(),                  name='per_viewen'),
	path('product-detail/<slug:slug>/',  		                   view=ProductDetailENView.as_view(),          name='per_detail_viewen'),

	path('dis-ortam/cadde-aydinlatmasi/',                          view=ProductTrCaddBView.as_view(),           name='dis_cadde'),
	path('dis-ortam/lineer-ledtube-volans/',                       view=ProductTrLineerLedView.as_view(),       name='linner_led'),
	path('dis-ortam/projector/',                                   view=ProductTrProjectorView.as_view(),       name='projector'),
	path('dis-ortam/el-feneri/',                                   view=ProductTrElfeView.as_view(),            name='el-feneri'),
	path('dis-ortam/bahce-park-aydinlatmasi/',                     view=ProductTrParkView.as_view(),            name='park'),
	path('dis-ortam/wallwasher/',                                  view=ProductTrWallwasherView.as_view(),      name='wallwasher'),
	path('dis-ortam/mobil-isik-kulesi/',                           view=ProductTrMobisView.as_view(),           name='mobil-isik-kulesi'),
	path('dis-ortam/dot-led-scorpius/',                            view=ProductTrDotLedView.as_view(),          name='dot-led-scorpius'),
	path('dis-ortam/arac-ustu-isik-kulesi/',                       view=ProductTrAracUstuView.as_view(),        name='arac-ustu-isik-kulesi'),
	path('dis-ortam/portatif-alan-aydinlatmasi/',                  view=ProductTrPorTatifUFLEDView.as_view(),   name='ufled'),
	path('dis-ortam/moduler-led-aydinlatmas-seti/',                view=ProductTrYBTsedView.as_view(),          name='ybtsed'),
	path('dis-ortam/dekoratif-led-ampul/',                         view=ProductTrDekredampulView.as_view(),     name='dek-led-ampul'),
	path('dis-ortam/aksesuarlar/',                                 view=ProductTrAksesuarlarView.as_view(),     name='aksesuarlar'),

	path('outdoor-products/cadde-aydinlatmasi/',                          view=ProductCaddBView.as_view(),           name='dis_caddeen'),
	path('outdoor-products/lineer-ledtube-volans/',                       view=ProductLineerLedView.as_view(),       name='linner_leden'),
	path('outdoor-products/projector/',                                   view=ProductProjectorView.as_view(),       name='projectoren'),
	path('outdoor-products/el-feneri/',                                   view=ProductElfeView.as_view(),            name='el-fenerien'),
	path('outdoor-products/bahce-park-aydinlatmasi/',                     view=ProductParkView.as_view(),            name='parken'),
	path('outdoor-products/wallwasher/',                                  view=ProductWallwasherView.as_view(),      name='wallwasheren'),
	path('outdoor-products/mobil-isik-kulesi/',                           view=ProductMobisView.as_view(),           name='mobil-isik-kulesien'),
	path('outdoor-products/dot-led-scorpius/',                            view=ProductDotLedView.as_view(),          name='dot-led-scorpiusen'),
	path('outdoor-products/arac-ustu-isik-kulesi/',                       view=ProductAracUstuView.as_view(),        name='arac-ustu-isik-kulesien'),
	path('outdoor-products/portatif-alan-aydinlatmasi/',                  view=ProductPorTatifUFLEDView.as_view(),   name='ufleden'),
	path('outdoor-products/moduler-led-aydinlatmas-seti/',                view=ProductYBTsedView.as_view(),          name='ybtseden'),
	path('outdoor-products/dekoratif-led-ampul/',                         view=ProductDekredampulView.as_view(),     name='dek-led-ampulen'),
	path('outdoor-products/aksesuarlar/',                                 view=ProductAksesuarlarView.as_view(),     name='aksesuarlaren'),


	path('ic-ortam/dekoratif-led-ampul/',                          view=ProductTrDekredampulIcView.as_view(),   name='dek-led-ampul-ic'),
	path('ic-ortam/yuksek-tavan-led-aydinlatmasi/',                view=ProductTrYuksekTavansedView.as_view(),  name='yuk-tav-led'),
	path('ic-ortam/dekoratif-led-aydinlatma-seti/',                view=ProductTrDekoratifLedView.as_view(),    name='dek-led-ayd-seti'),

	path('indoor-products/dekoratif-led-ampul/',                          view=ProductDekredampulIcView.as_view(),   name='dek-led-ampul-icen'),
	path('indoor-products/yuksek-tavan-led-aydinlatmasi/',                view=ProductYuksekTavansedView.as_view(),  name='yuk-tav-leden'),
	path('indoor-products/dekoratif-led-aydinlatma-seti/',                view=ProductDekoratifLedView.as_view(),    name='dek-led-ayd-setien'),

	path('yardimci-urunler/cob-led-modül-armekeddon/',             view=ProductTrCobledView.as_view(),          name='cobled'),
	path('yardimci-urunler/waterproof-connectorler/',              view=ProductTrVaterProfConView.as_view(),    name='waterprof'),
	path('yardimci-urunler/waterproof-enerji-dagitici/',           view=ProductTrVaterProfEnerView.as_view(),   name='waterprofener'),

	path('auxiliary-products/cob-led-modül-armekeddon/',             view=ProductCobledView.as_view(),          name='cobleden'),
	path('auxiliary-products/waterproof-connectorler/',              view=ProductVaterProfConView.as_view(),    name='waterprofen'),
	path('auxiliary-products/waterproof-enerji-dagitici/',           view=ProductVaterProfEnerView.as_view(),   name='waterprofeneren'),

	path('galeri/',                                              view=ProjectsTRView.as_view(),               name='project'),
	path('proje-detay/<slug:slug>/',                               view=ProjectsDetailTrView.as_view(),         name='proje_detay'),
	

	path('projeler/spor-tesisleri/',                                view=ProjectsSportTRView.as_view(),         name='spor'),
	path('projeler/gayrimenkul-insaat/',                            view=ProjectsGayrTRView.as_view(),          name='gayin'),
	path('projeler/halka-acik-alanlar/',                            view=ProjectsHalkTRView.as_view(),          name='halac'),
	path('projeler/ozel-kurumlar/',                                 view=ProjectsOzkTRView.as_view(),           name='ozkur'),
	path('projeler/kamu-kurumlari/',                                view=ProjectsKamuTRView.as_view(),          name='kamu'),
	
	path('projects/',                             	                view=ProjectsView.as_view(),                name='projecten'),
	path('project-detail/<slug:slug>/',                             view=ProjectsDetailENView.as_view(),        name='project-detail'),

	path('projeler/sports-facilities/',                             view=ProjectsSportView.as_view(),           name='sporen'),
	path('projeler/real-estate-and-construction/',                  view=ProjectsGayrView.as_view(),            name='gayinen'),
	path('projeler/public-areas/',                             		view=ProjectsHalkView.as_view(),            name='halacen'),
	path('projeler/private-instituions/',                           view=ProjectsOzkView.as_view(),             name='ozkuren'),
	path('projeler/public-instituions/',                            view=ProjectsKamuView.as_view(),            name='kamuen'),

]