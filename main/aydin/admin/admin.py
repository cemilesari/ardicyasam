 
from __future__ import unicode_literals, absolute_import
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from main.aydin.models import *


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
	list_display = ( "title","body", "created",)
	date_hierarchy = "created"



@admin.register(BlogTr)
class BlogAdmin_Tr(admin.ModelAdmin):
	list_display = ("title", "created",)
	search_fields = ("title",) 
	date_hierarchy = "created"

@admin.register(AboutTR)
class AboutTRAdmin(admin.ModelAdmin):
	list_display = ("title","image","created",)
	search_fields = ("title",) 
	date_hierarchy = "created"

@admin.register(HomeSeo)
class HomeSeoAdmin(admin.ModelAdmin):
	list_display = ("titlesite","created",)
	search_fields = ("title",) 
	date_hierarchy = "created"


@admin.register(ProjectsTRSeoTR)
class ProjectSeoAdmin(admin.ModelAdmin):
	list_display = ("titlesite","created",)
	search_fields = ("title",) 
	date_hierarchy = "created"
@admin.register(ProjectsSeoTR)
class ProjectTRSeoAdmin(admin.ModelAdmin):
	list_display = ("titlesite","created",)
	search_fields = ("title",) 
	date_hierarchy = "created"

@admin.register(İletisimSeoTR)
class İletisimSeoTRAdmin(admin.ModelAdmin):
	list_display = ("titlesite","created",)
	search_fields = ("title",) 
	date_hierarchy = "created"

@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
	list_display = ("full_name","body","created",)
	search_fields = ("title",) 
	date_hierarchy = "created"

@admin.register(BlogSeoPageModel)
class BlogSeoPageAdmin(admin.ModelAdmin):
	list_display = ("title","created",)
	search_fields = ("title",) 
	date_hierarchy = "created"

@admin.register(Products)
class ProductsENAdmin(admin.ModelAdmin):
	list_display = ("title","body","created",)
	search_fields = ("title",) 
	date_hierarchy = "created"

@admin.register(KeywordsTR)
class KeywordsTR(admin.ModelAdmin):
	pass

@admin.register(ProductsTr)
class ProductsTrAdmin(admin.ModelAdmin):
	list_display = ("title","created",)
	search_fields = ("title",) 
	date_hierarchy = "created"
	
@admin.register(Projects)
class ProjectsENAdmin(admin.ModelAdmin):
	list_display = ("title","category","created",)
	search_fields = ("title",) 
	date_hierarchy = "created"
@admin.register(Category)
class ProjCatENAdmin(admin.ModelAdmin):
	list_display = ("name","created",)
	search_fields = ("name",) 
	date_hierarchy = "created"

@admin.register(ProjectsTR)
class ProjectsTRAdmin(admin.ModelAdmin):
	list_display = ("title","created",)
	search_fields = ("title",) 
	date_hierarchy = "created"
@admin.register(CategoryTR)
class ProjCatTRAdmin(admin.ModelAdmin):
	list_display = ("name","created",)
	search_fields = ("name",) 
	date_hierarchy = "created"
@admin.register(ProductCategoryTR)
class ProductCategoryTRTRAdmin(admin.ModelAdmin):
	list_display = ("name","created",)
	search_fields = ("name",) 
	date_hierarchy = "created"
@admin.register(ProductCategory)
class ProductCategoryTRAdmin(admin.ModelAdmin):
	list_display = ("name","created",)
	search_fields = ("name",) 
	date_hierarchy = "created"


