from django.contrib import admin
from users_app.models import users_list,owes,owed_by,balance
# Register your models here.,admin
admin.site.register(users_list)
admin.site.register(owes)
admin.site.register(owed_by)
admin.site.register(balance)


