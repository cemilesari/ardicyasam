

from __future__ import unicode_literals
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.conf import settings
from main.core.models import TimeStampedModel, Currency
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from .blog import *
class HomeSeo(TimeStampedModel):
    class Meta:
        verbose_name = _("Ana Sayfa Seo")
        verbose_name_plural = _("Ana Sayfa Seo")
        ordering = ("-created",)
    titlesite = models.CharField(_("Site Başlık"), max_length=200,blank=True, null=True)
    description = models.CharField(_("Meta Açıklama"), max_length=200,blank=True, null=True)
    keywords =  models.ManyToManyField(Keywords, verbose_name=_("Anahtar Kelimeler"),blank=True, null=True)
    def __str__(self):
        return self.titlesite

class İletisimSeo(TimeStampedModel):
    class Meta:
        verbose_name = _("EN SEO İletisim")
        verbose_name_plural = _("EN SEO İletisim")
        ordering = ("-created",)
    titlesite = models.CharField(_("Site Title"), max_length=200,blank=True, null=True)
    description = models.CharField(_("Meta Description"), max_length=200,blank=True, null=True)
    keywords =  models.ManyToManyField(Keywords, verbose_name=_("Keywords"),blank=True, null=True)
    def __str__(self):
        return self.titlesite
class İletisimSeoTR(TimeStampedModel):
    class Meta:
        verbose_name = _("İletisim Seo")
        verbose_name_plural = _("İletisim Seo")
        ordering = ("-created",)
    titlesite = models.CharField(_("Site Title"), max_length=200,blank=True, null=True)
    description = models.CharField(_("Meta Description"), max_length=200,blank=True, null=True)
    keywords =  models.ManyToManyField(KeywordsTR, verbose_name=_("Keywords"),blank=True, null=True)
    def __str__(self):
        return self.titlesite
class ProjectsSeoTR(TimeStampedModel):
    class Meta:
        verbose_name = _("EN SEO Projeler")
        verbose_name_plural = _("EN SEO Projeler")
        ordering = ("-created",)
    titlesite = models.CharField(_("Site Title"), max_length=200,blank=True, null=True)
    description = models.CharField(_("Meta Description"), max_length=200,blank=True, null=True)
    keywords =  models.ManyToManyField(KeywordsTR, verbose_name=_("Keywords"),blank=True, null=True)
    def __str__(self):
        return self.titlesite
class ProjectsTRSeoTR(TimeStampedModel):
    class Meta:
        verbose_name = _("SEO Galeri")
        verbose_name_plural = _("TR SEO Projeler")
        ordering = ("-created",)
    titlesite = models.CharField(_("Site Title"), max_length=200,blank=True, null=True)
    description = models.CharField(_("Meta Description"), max_length=200,blank=True, null=True)
    keywords =  models.ManyToManyField(KeywordsTR, verbose_name=_("Keywords"),blank=True, null=True)
    def __str__(self):
        return self.titlesite