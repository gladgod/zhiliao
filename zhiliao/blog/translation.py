from modeltranslation.translator import translator
from zhiliao.core.translation import (TranslatedSlugged,
                                        TranslatedDisplayable,
                                        TranslatedRichText)
from zhiliao.blog.models import BlogCategory, BlogPost


class TranslatedBlogPost(TranslatedDisplayable, TranslatedRichText):
    fields = ()


class TranslatedBlogCategory(TranslatedSlugged):
    fields = ()

translator.register(BlogCategory, TranslatedBlogCategory)
translator.register(BlogPost, TranslatedBlogPost)
