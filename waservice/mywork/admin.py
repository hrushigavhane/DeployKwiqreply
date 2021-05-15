from __future__ import unicode_literals

from django.contrib import admin

from .models import User_Details, Business_Profile, Submit_Ticket, Sales, Sandbox_Names, Sandbox_Webhook

admin.site.register(User_Details)
admin.site.register(Business_Profile)
admin.site.register(Submit_Ticket)
admin.site.register(Sales)
admin.site.register(Sandbox_Names)
admin.site.register(Sandbox_Webhook)
