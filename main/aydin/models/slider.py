from __future__ import unicode_literals
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.conf import settings
from main.core.models import TimeStampedModel, Currency
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Slider(TimeStampedModel):
    class Meta:
        verbose_name = _("0-Slider ")
        verbose_name_plural = _("0-Sliderlar")
        ordering = ("-created",)
    title  = models.CharField(_("Başlık"), max_length=200,)
    body   = models.TextField(_("Slider Body"), blank=True)
    sliderimage  = models.ImageField(_("Slider Image"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True, default=settings.DEFAULT_BLOG_IMAGE)
    def __str__(self):
        return self.title

class SliderEN(TimeStampedModel):
    class Meta:
        verbose_name = _(" EN Slider ")
        verbose_name_plural = _("EN Sliderlar")
        ordering = ("-created",)
    title  = models.CharField(_("Başlık"), max_length=200,)
    body   = models.TextField(_("Slider Body"), blank=True)
    button = models.CharField(_("Slider Button Url"), max_length=300,)
    sliderimage  = models.ImageField(_("Slider Image"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True, default=settings.DEFAULT_BLOG_IMAGE)
    def __str__(self):
        return self.title
