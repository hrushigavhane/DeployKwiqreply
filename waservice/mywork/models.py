# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class User_Details(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=100, blank=False)
    password = models.TextField()
    username = models.EmailField()
    comp_name = models.CharField(max_length=100, blank=False)
    is_active = models.BooleanField(default=False)
    user_img = models.ImageField(upload_to='pics')
    sent_message = models.BooleanField(default=False)

    # logged_in = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Registered Users"


class Business_Profile(models.Model):
    # select_number = models.CharField(max_length=10, blank=False)
    # display_name = models.CharField(max_length=100, blank=False)
    # facebook_id = models.CharField(max_length=100, blank=False)
    # comp_addr = models.CharField(max_length=100, null=True)
    # comp_email = models.EmailField()
    # website = models.CharField(max_length=100, null=True)
    # logo = models.CharField(max_length=100, null=True)
    # user = models.ForeignKey('User_Details', on_delete=models.CASCADE)

    Comp_name = models.CharField(max_length=40, blank=False, default="Company name")
    Business_desc = models.CharField(max_length=200, blank=False, default="Default description")
    Business_Category = models.CharField(max_length=40, blank=False, default="Others")
    facebook_id = models.CharField(max_length=40, blank=False, default="Facebook id")
    business_disp_name = models.CharField(max_length=40, blank=False, default="disp name")
    about_business = models.CharField(max_length=200, blank=False, default="About")
    business_address = models.CharField(max_length=200, blank=False, default="Company address")
    business_email = models.EmailField()
    business_number = models.CharField(max_length=15, blank=False, default=91123456879)
    radio = models.CharField(max_length=3, blank=False, default="yes")
    website = models.CharField(max_length=200, blank=False, default="website")
    user = models.ForeignKey('User_Details', on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Business Profile Form Submission Data"


class Submit_Ticket(models.Model):
    subject = models.CharField(max_length=100, blank=False)
    comment = models.CharField(max_length=1000, blank=False)
    product = models.CharField(max_length=100, blank=False)
    business_impact = models.CharField(max_length=100, blank=False)
    ticketdate = models.DateField()
    user = models.ForeignKey('User_Details', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Ticket Form Submission Data"


class Sales(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField()
    comp_name = models.CharField(max_length=100, blank=False)
    job = models.CharField(max_length=100, blank=False)
    phone_number = models.CharField(max_length=100, blank=False)
    country = models.CharField(max_length=100, blank=False)
    state = models.CharField(max_length=100, blank=False)
    user = models.ForeignKey('User_Details', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Sales Form Submission Data"


class Sandbox_Names(models.Model):
    username = models.EmailField()
    code = models.CharField(max_length=100, blank=False)

    # user = models.ForeignKey('User_Details', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Sandbox Names For Clients"


class Sandbox_Webhook(models.Model):
    webhook = models.CharField(max_length=1000, blank=False)
    phone = models.CharField(max_length=100, blank=False)
    user = models.ForeignKey('User_Details', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Sandbox Client Webook URL"


class user_message(models.Model):
    wa_id = models.CharField(max_length=15, blank=False)
    name = models.CharField(max_length=50)
    message = models.TextField(blank=True)
    m_type = models.CharField(max_length=12)
    m_url = models.CharField(max_length=1000, blank=True)
    m_service = models.CharField(max_length=15, blank=True)
    m_fileName = models.CharField(max_length=100, blank=True)
    m_from = models.CharField(max_length=15)
    m_status = models.CharField(max_length=10, blank=True)
    m_media = models.TextField(blank=True)
    m_previous = models.CharField(max_length=5, blank=True)
    m_current = models.CharField(max_length=5, blank=True)
    m_session = models.CharField(max_length=8, default='')
    timestamp1 = models.DateTimeField()
    caption = models.TextField(blank=True)
    unique_msg_id = models.CharField(max_length=35,blank=False,default="")
    unique_msg_status = models.CharField(max_length=10,blank=True,default='sent')

    class Meta:
        verbose_name_plural = "User Mesages"


class template_master(models.Model):
    temp_id = models.AutoField(primary_key=True)
    namespace = models.CharField(max_length=30, blank=False)
    temp_name = models.CharField(max_length=50, blank=False)
    temp_payload = models.TextField(blank=False)

# Create your models here.
