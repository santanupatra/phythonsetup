# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import User
from models import *

# Register your models here.
# admin.site.register(User)
# admin.site.unregister(User)
print (User.objects.all()[0].email)
admin.site.site_header = "Scottie Thompson Live Stream Admin"
admin.site.site_title = "Scottie Thompson Live Stream Admin"

admin.site.register(UserProfile)
admin.site.register(Role)
admin.site.register(PointResult)
admin.site.register(BlogCategorie)
admin.site.register(Blog)
admin.site.register(BlogComment)