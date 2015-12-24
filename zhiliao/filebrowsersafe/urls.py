from __future__ import unicode_literals

from django.conf.urls import *

urlpatterns = patterns('',

    # filebrowser urls
    url(r'^browse/$', 'zhiliao.filebrowsersafe.views.browse', name="fb_browse"),
    url(r'^mkdir/', 'zhiliao.filebrowsersafe.views.mkdir', name="fb_mkdir"),
    url(r'^upload/', 'zhiliao.filebrowsersafe.views.upload', name="fb_upload"),
    url(r'^rename/$', 'zhiliao.filebrowsersafe.views.rename', name="fb_rename"),
    url(r'^delete/$', 'zhiliao.filebrowsersafe.views.delete', name="fb_delete"),
    url(r'^check_file/$', 'zhiliao.filebrowsersafe.views._check_file', name="fb_check"),
    url(r'^upload_file/$', 'zhiliao.filebrowsersafe.views._upload_file', name="fb_do_upload"),

)
