from django.contrib import admin
from . models import Form, UserQuery

from simple_history.admin import SimpleHistoryAdmin

admin.site.register(UserQuery, SimpleHistoryAdmin)
admin.site.register(Form)

