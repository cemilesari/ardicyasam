 
from __future__ import unicode_literals
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.conf import settings
from main.core.models import TimeStampedModel, Currency
from autoslug import AutoSlugField
from embed_video.fields import EmbedVideoField
from ckeditor_uploader.fields import RichTextUploadingField
from main.aydin.models.blog import *
class CertificaEN(TimeStampedModel):
    class Meta:
        verbose_name = _("EN Sertifika")
        verbose_name_plural = _("EN Sertifikalar")
        ordering = ("-created",)
    
    name    = models.CharField(_("Başlık"), max_length=200,)
    body     = models.FileField(_("Sertifika"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True)
    
    def __str__(self):
        return self.name
class BrosEN(TimeStampedModel):
    class Meta: 
        verbose_name = _("EN Broşür")
        verbose_name_plural = _("EN Broşürler")
        ordering = ("-created",)
    name    = models.CharField(_("Başlık"), max_length=200,)
    body     = models.FileField(_("Broşür"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True)
    def __str__(self):
        return self.name
class KlavuzEN(TimeStampedModel):
    class Meta: 
        verbose_name = _("EN Kullanım Klavuzu")
        verbose_name_plural = _("EN Kullanım Klavuzları")
        ordering = ("-created",)
    name    = models.CharField(_("Başlık"), max_length=200,)
    body     = models.FileField(_("Kullanım Klavuzu"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True)
    def __str__(self):
        return self.name
class ProductSlider(TimeStampedModel):
    class Meta: 
        verbose_name = "Ürün Slider"
        verbose_name_plural = "Ürün Sliderları"
    name  = models.CharField(_("Slider İsim"), max_length=200,)
    image = models.ImageField(_("Ürün Resim"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True, default=settings.DEFAULT_BLOG_IMAGE)
    def __str__(self):
        return self.name
class ProductCategory(TimeStampedModel):
    class Meta:
        verbose_name = _("EN Ürünler Alt Categori")
        verbose_name_plural = _("EN Ürünler Alt Categori ")
        ordering = ("-created",)
    name = models.CharField(_("Categori İsmi"), max_length=200,)
    #parent_category = models.ForeignKey(SubCategoryTR, null=True, blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class Products(TimeStampedModel):
    class Meta:
        verbose_name = _("EN Ürün")
        verbose_name_plural = _("EN Ürünler ")
        ordering = ("-created",)
    DIS        = "DIŞ ORTAM"
    IC         = "İÇ ORTAM"
    YRD         = "YARDIMCI ÜRÜNLER"
    CATEGORY = (
        (DIS        , _("DIŞ ORTAM")),
        (IC   , _("İÇ ORTAM")),
        (YRD         , _("YARDIMCI ÜRÜNLER")),
    )
    title    = models.CharField(_("Başlık"), max_length=200,)
    body     = models.TextField(_("Ürün Yazı"), blank=True)
    image    = models.ImageField(_("Ürün Resim"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True, default=settings.DEFAULT_BLOG_IMAGE)
    slider    = models.ManyToManyField(ProductSlider, verbose_name=_("Ürün Slider"),blank=True, null=True)
    tek_body   = RichTextUploadingField(_("Teknik Özellikler"), blank=True)
    category = models.CharField(_("Kategori Seçiniz"),choices=CATEGORY, default=DIS, max_length=500)
    subcategory = models.ForeignKey(ProductCategory, verbose_name=_("Alt Kategori"),blank=True,null=True,on_delete=models.CASCADE)
    dowloads   = models.ForeignKey(KlavuzEN, verbose_name=_("Dökümanlar"),blank=True,null=True,on_delete=models.CASCADE)
    kod    = models.CharField(_("Ürün Kodu"), max_length=200,blank=True, null=True,)
    video   = EmbedVideoField(blank=True) 
    slug   = models.SlugField(max_length=100)
    titlesite = models.CharField(_("Site Title"), max_length=200,blank=True, null=True)
    description = models.CharField(_("Meta Description"), max_length=200,blank=True, null=True)
    keywords =  models.ManyToManyField(Keywords, verbose_name=_("Keywords"),blank=True, null=True)

    def __str__(self):
        return self.title


class Certifica(TimeStampedModel):
    verbose_name = _("TR Sertifika")
    verbose_name_plural = _("TR Sertifikalar")
    ordering = ("-created",)
    
    name    = models.CharField(_("Başlık"), max_length=200,)
    body     = models.FileField(_("Sertifika"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True)
    
    def __str__(self):
        return self.name
class Bros(TimeStampedModel):
    class Meta:
        verbose_name = _("TR Broşür")
        verbose_name_plural = _("TR Broşürler")
        ordering = ("-created",)
    name    = models.CharField(_("Başlık"), max_length=200,)
    body     = models.FileField(_("Broşür"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True)
    def __str__(self):
        return self.name
class Klavuz(TimeStampedModel):
    verbose_name = _("TR Kullanım Klavuzu")
    verbose_name_plural = _("TR Kullanım Klavuzları")
    ordering = ("-created",)
    name    = models.CharField(_("Başlık"), max_length=200,)
    body     = models.FileField(_("Kullanım Klavuzu"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True)
    def __str__(self):
        return self.name
class ProductCategoryTR(TimeStampedModel):
    class Meta:
        verbose_name = _(" 1.1-Ürünler  Kategori")
        verbose_name_plural = _("1.1-Ürünler Kategori ")
        ordering = ("ordering",)
    name = models.CharField(_("Categori İsmi"), max_length=200,)
    description = RichTextUploadingField(_(" Açıklama"),blank=True, null=True)
    ordering = models.PositiveIntegerField(null=True, blank=True, default=1)


    def __str__(self):
        return self.name
    

class Teams(TimeStampedModel):
    class Meta:
        verbose_name = _(" 6-Ekibimiz")
        verbose_name_plural = _("6- Ekibimiz")
        ordering = ("ordering",)
    name = models.CharField(_("İsim"), max_length=200,)
    name1 = models.CharField(_("Görevi"), max_length=200,)
    image    = models.ImageField(_(" Resim"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True, default=settings.DEFAULT_BLOG_IMAGE)
    description = RichTextUploadingField(_("Detaylı Bilgi"),blank=True, null=True)
    ordering = models.PositiveIntegerField(null=True, blank=True, default=1)


    def __str__(self):
        return self.name
    
class ProductsTr(TimeStampedModel):
    class Meta:
        verbose_name = _("1-Ürün ")
        verbose_name_plural = _("1-Ürünler")
        ordering = ("-created",)

    title    = models.CharField(_("Başlık"), max_length=200,)
    body     = RichTextUploadingField(_("Ürün Yazı"), blank=True)
    image    = models.ImageField(_("Ürün Resim"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True, default=settings.DEFAULT_BLOG_IMAGE)
    #slider    = models.ManyToManyField(ProductSlider, verbose_name=_("Ürün Slider"),blank=True, null=True)
    tek_body   = RichTextUploadingField(_("Teknik Özellikler"), blank=True)
    subcategory = models.ForeignKey(ProductCategoryTR, verbose_name=_(" Kategori"),blank=True,null=True,on_delete=models.CASCADE)
    kod    = models.CharField(_("Ürün Kodu"), max_length=200,blank=True, null=True,)
    slug   = models.SlugField(max_length=100)
    titlesite = models.CharField(_("Site Title"), max_length=200,blank=True, null=True)
    description = models.CharField(_("Meta Description"), max_length=200,blank=True, null=True)
    keywords =  models.ManyToManyField(KeywordsTR, verbose_name=_("Keywords"),blank=True, null=True)
    fiyat    = models.CharField(_("Fiyat"), max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title