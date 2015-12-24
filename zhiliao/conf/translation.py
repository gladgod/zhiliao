from modeltranslation.translator import translator, TranslationOptions
from zhiliao.conf.models import Setting


class TranslatedSetting(TranslationOptions):
    fields = ('value',)

translator.register(Setting, TranslatedSetting)
