from __future__ import unicode_literals
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.conf import settings
from main.core.models import TimeStampedModel, Currency
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from .blog import *
class About(TimeStampedModel):
    class Meta:
        verbose_name = _("EN Hakkımızda")
        verbose_name_plural = _("EN Hakkımızda")
        ordering = ("-created",)
    title  = models.CharField(_("Title"), max_length=200,blank=True,null=True)
    body   = RichTextUploadingField(_("About Body"), blank=True)
    image  = models.ImageField(_("About Image"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True, default=settings.DEFAULT_BLOG_IMAGE)
    slug = models.SlugField(max_length=100)
    titlesite = models.CharField(_("Site Title"), max_length=200,blank=True, null=True)
    description = models.CharField(_("Meta Description"), max_length=200,blank=True, null=True)
    keywords =  models.ManyToManyField(Keywords, verbose_name=_("Keywords"),blank=True, null=True)

    def __str__(self):
        return self.title

    def get_dict(self):
        return dict(
            pk    = self.pk,
            title = self.title,
            body  = self.body,
            image = self.image,
            slug  = self.slug,

        )
class AboutTR(TimeStampedModel):
    class Meta:
        verbose_name = _("4-Hakkımızda ")
        verbose_name_plural = _("4-Hakkımızda")
        ordering = ("-created",)
    title  = models.CharField(_("Başlık"), max_length=200,blank=True,null=True)
    body   = RichTextUploadingField(_("Hakkımızda Body"), blank=True)
    image  = models.ImageField(_("Hakkımızda Resim"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True, default=settings.DEFAULT_BLOG_IMAGE)
    titlesite = models.CharField(_("Site Başlık"), max_length=200,blank=True, null=True)
    description = models.CharField(_("Meta Açıklama"), max_length=200,blank=True, null=True)
    keywords =  models.ManyToManyField(KeywordsTR, verbose_name=_("Keywords"),blank=True, null=True)
    def __str__(self):
        return self.title

    def get_dict(self):
        return dict(
            pk    = self.pk,
            title = self.title,
            body  = self.body,
            image = self.image,
            slug  = self.slug,
        )