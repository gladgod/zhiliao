from __future__ import unicode_literals

from django.contrib import admin

from zhiliao.core.admin import TabularDynamicInlineAdmin
from zhiliao.pages.admin import PageAdmin
from zhiliao.galleries.models import Gallery, GalleryImage
from zhiliao.utils.static import static_lazy as static


class GalleryImageInline(TabularDynamicInlineAdmin):
    model = GalleryImage


class GalleryAdmin(PageAdmin):

    class Media:
        css = {"all": (static("zhiliao/css/admin/gallery.css"),)}

    inlines = (GalleryImageInline,)


admin.site.register(Gallery, GalleryAdmin)
