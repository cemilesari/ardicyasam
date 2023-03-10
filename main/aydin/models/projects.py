 
from __future__ import unicode_literals
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.conf import settings
from main.core.models import TimeStampedModel, Currency
from autoslug import AutoSlugField
from embed_video.fields import EmbedVideoField
from ckeditor_uploader.fields import RichTextUploadingField
from main.aydin.models.blog import *
from main.aydin.models.products import *

class ProjectSlider(TimeStampedModel):
    class Meta: 
        verbose_name = "Ürün Slider"
        verbose_name_plural = "Ürün Sliderları"
    name  = models.CharField(_("Slider İsim"), max_length=200,)
    image = models.ImageField(_("Ürün Resim"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True, default=settings.DEFAULT_BLOG_IMAGE)
    def __str__(self):
        return self.name
class Category(TimeStampedModel):
    class Meta:
        verbose_name = _("EN Proje Categori")
        verbose_name_plural = _("EN Proje Categori ")
        ordering = ("-created",)
    name = models.CharField(_("Categori İsmi"), max_length=200,)
    #parent_category = models.ForeignKey(SubCategoryTR, null=True, blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class Projects(TimeStampedModel):
    class Meta:
        verbose_name = _("EN Projeler")
        verbose_name_plural = _("EN Projeler ")
        ordering = ("-created",)
    title    = models.CharField(_("Başlık"), max_length=200,)
    tek_body   = RichTextUploadingField(_("Proje Açıklama"), blank=True)
    tek_body2   = RichTextUploadingField(_("Proje Detay Açıklama"), blank=True)
    image    = models.ImageField(_("Ürün Resim"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True, default=settings.DEFAULT_BLOG_IMAGE)
    image_home  = models.ImageField(_("Ürün Ana Sayfa Resim"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True, default=settings.DEFAULT_BLOG_IMAGE)
    slider    = models.ManyToManyField(ProjectSlider, verbose_name=_("Ürün Slider"),blank=True, null=True)
    category   = models.ForeignKey(Category, verbose_name=_("Select Category"),blank=True,null=True,on_delete=models.CASCADE)
    products = models.ManyToManyField(Products, verbose_name=_("Products"),blank=True, null=True)
    slug   = models.SlugField(max_length=100)
    titlesite = models.CharField(_("Site Title"), max_length=200,blank=True, null=True)
    description = models.CharField(_("Meta Description"), max_length=200,blank=True, null=True)
    keywords =  models.ManyToManyField(KeywordsTR, verbose_name=_("Keywords"),blank=True, null=True)

    def __str__(self):
        return self.title


#class SubCategoryTR(TimeStampedModel):
#    class Meta:
#        verbose_name = _("TR Proje Alt Categori")
#        verbose_name_plural = _("TR Proje Alt Categori ")
#        ordering = ("-created",)
#    name = models.CharField(_("Alt Categori İsmi"), max_length=200,)
#    def __str__(self):
#        return self.name

class CategoryTR(TimeStampedModel):
    class Meta:
        verbose_name = _("TR Proje Categori")
        verbose_name_plural = _("TR Proje Categori ")
        ordering = ("-created",)
    name = models.CharField(_("Categori İsmi"), max_length=200,)
    #parent_category = models.ForeignKey(SubCategoryTR, null=True, blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class ProjectsTR(TimeStampedModel):
    class Meta:
        verbose_name = _("Galeri")
        verbose_name_plural = _("Galeri ")
        ordering = ("-created",)
    title    = models.CharField(_("Başlık"), max_length=200,)
    image    = models.ImageField(_("Ürün Resim"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True, default=settings.DEFAULT_BLOG_IMAGE)

    def __str__(self):
        return self.title

