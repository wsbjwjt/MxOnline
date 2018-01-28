# -*- coding: utf-8 -*-
__author__ = 'Eric Wang'
__date__ = '2018/1/28 12:18'

import xadmin
# from .models import UserProfile
from .models import EmailVerifyRecord, Banner


# class UserProfileAdmin(object):
#     pass
#
#
# xadmin.site.register(UserProfile, UserProfileAdmin)

# 创建admin的管理类,这里不再是继承admin，而是继承object
class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type', 'send_time']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)