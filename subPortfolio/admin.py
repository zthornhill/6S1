from django.contrib import admin
from .models import User, Subscription


class UserList(admin.ModelAdmin):
    list_display = ('acctNum', 'username', 'city', 'phoneNum')
    list_filter = ('acctNum', 'username', 'city')
    search_fields = ('acctNum', 'username')
    ordering = ['acctNum']


class SubscriptionList(admin.ModelAdmin):
    list_display = ('user', 'sub_Name', 'sub_Description', 'sub_Price')
    list_filter = ('user', 'sub_Name')
    search_fields = ('user', 'sub_Name')
    ordering = ['user']


admin.site.register(User, UserList)
admin.site.register(Subscription, SubscriptionList)
