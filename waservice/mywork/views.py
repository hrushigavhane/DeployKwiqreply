

import csv
import datetime
import os
import sys
import uuid
import calendar
import time
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import User, auth
from django.contrib.sites.shortcuts import get_current_site
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.db import connection
from django.db.models.expressions import Subquery
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
import json
import random
import urllib.request
import requests
import base64
import mimetypes
from urllib.parse import urlparse
from django.core import serializers
from django.utils import timezone


from .models import User_Details, Business_Profile, Submit_Ticket, Sales, Sandbox_Names, Sandbox_Webhook ,user_message,template_master
from .tokens import account_activation_token

#***********************************By Shubham For Framework.py****************************************
import threading
# from django.conf import settings
import django
# from ktech import ktech
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode


from django.views.decorators.csrf import csrf_exempt

# Create your views here.
#login_user = User_Details.objects.raw('select * from mywork_user_details where username=%s',[username])[0]
#login_user.username == "ktpl.tech@gmail.com":

current_user={'username':'', 'password':'', 'first_name':'', 'last_name':'', 'comp_name':'','phone':'', 'is_active':False}
url_main = "https://3.137.182.68:9090"
pass_for_api = "Khairnar@1234!"
base_64 = "YWRtaW46S2hhaXJuYXJAMTIzNCE="
email_of_off = "noreply@kwiqreply.io"

def home(request):
    print(request)
    return render(request, 'index.html')

# ----------ADMIN SECTION-------------#

def admin_section(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            id_no = User.objects.filter(username=username)[0]
            print(id_no)
            request.session['admin'] = True
            request.session['id'] = id_no.id

            return redirect('admin_panel')

        else:
            messages.info(request, 'Check your details..')
            return redirect('admin_section')
    else:
        return render(request,  'admin_section.html')

def admin_panel(request):
    response=""
    response1=""

    if request.session.get('id'):
        user_id = request.session.get('id')
        response += "User Id : {0}".format(user_id)
        print(response)

    if request.session.get('admin'):
        admin_flag = request.session.get('admin')
        response1 += "Admin : {0}".format(admin_flag)
        print(response1)

    else:
        admin_flag = False
        response1 += "Admin : {0}".format(admin_flag)
        print(response1)

    if not response or not response1:
        return render(request, 'index.html')

    else:
        if admin_flag:
            auth_user_count = User.objects.count()
            user_details_count = User_Details.objects.count()
            businessprofile_count = Business_Profile.objects.count()
            submit_ticket_count = Submit_Ticket.objects.count()
            sales_count = Sales.objects.count()
            sandboxweb_count = Sandbox_Webhook.objects.count()

            user_disp = User.objects.filter(id=request.session['id'])

            list_count = [auth_user_count, user_details_count, businessprofile_count, submit_ticket_count, sales_count, sandboxweb_count]
            return render(request,  'admin_panel.html', {'obj': user_disp, 'auth_user_count':list_count[0], 'user_details_count':list_count[1],'businessprofile_count':list_count[2], 'submit_ticket_count':list_count[3], 'sales_count':list_count[4], 'sandboxweb_count':list_count[5]})
        else:
            return render(request, 'index.html')


def admin_registered_user(request):
    response=""
    response1=""

    if request.session.get('id'):
        user_id = request.session.get('id')
        response += "User Id : {0}".format(user_id)
        print(response)

    if request.session.get('admin'):
        admin_flag = request.session.get('admin')
        response1 += "Admin : {0}".format(admin_flag)
        print(response1)

    else:
        admin_flag = False
        response1 += "Admin : {0}".format(admin_flag)
        print(response1)

    if not response or not response1:
        return render(request, 'index.html')

    else:
         if admin_flag:
             user_disp = User.objects.filter(id=request.session['id'])
             user_obj = User_Details.objects.all()
             return render(request,  'admin_registered_user.html', {'obj': user_disp, 'obj1': user_obj})
         else:
            return render(request, 'index.html')


def admin_ticket_submission(request):
    response=""
    response1=""

    if request.session.get('id'):
        user_id = request.session.get('id')
        response += "User Id : {0}".format(user_id)
        print(response)

    if request.session.get('admin'):
        admin_flag = request.session.get('admin')
        response1 += "Admin : {0}".format(admin_flag)
        print(response1)

    else:
        admin_flag = False
        response1 += "Admin : {0}".format(admin_flag)
        print(response1)

    if not response and not response1:
        return render(request, 'index.html')

    else:
        if admin_flag:
            user_disp = User.objects.filter(id=request.session['id'])
            user_obj = Submit_Ticket.objects.all()
            return render(request,  'admin_ticket_submission.html', {'obj': user_disp, 'obj1': user_obj})
        else:
           return render(request, 'index.html')


def admin_sale_submission(request):
    response=""
    response1=""

    if request.session.get('id'):
        user_id = request.session.get('id')
        response += "User Id : {0}".format(user_id)
        print(response)

    if request.session.get('admin'):
        admin_flag = request.session.get('admin')
        response1 += "Admin : {0}".format(admin_flag)
        print(response1)

    else:
        admin_flag = False
        response1 += "Admin : {0}".format(admin_flag)
        print(response1)

    if not response and not response1:
        return render(request, 'index.html')
    else:
        if admin_flag:
            user_disp = User.objects.filter(id=request.session['id'])
            user_obj = Sales.objects.all()
            return render(request,  'admin_sale_submission.html', {'obj': user_disp, 'obj1': user_obj})
        else:
           return render(request, 'index.html')

def admin_business_p(request):
    response=""
    response1=""

    if request.session.get('id'):
        user_id = request.session.get('id')
        response += "User Id : {0}".format(user_id)
        print(response)

    if request.session.get('admin'):
        admin_flag = request.session.get('admin')
        response1 += "Admin : {0}".format(admin_flag)
        print(response1)

    else:
        admin_flag = False
        response1 += "Admin : {0}".format(admin_flag)
        print(response1)

    if not response and not response1:
        return render(request, 'index.html')
    else:
        if admin_flag:
            user_disp = User.objects.filter(id=request.session['id'])
            user_obj = Business_Profile.objects.all()
            return render(request,  'admin_business_p.html', {'obj': user_disp, 'obj1': user_obj})
        else:
           return render(request, 'index.html')

# ----------USER SECTION-------------#

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        try:
            login_user = User_Details.objects.raw('select * from mywork_user_details where username=%s',[username])[0]
        except:
            messages.info(request, 'User not found')
            return redirect('login')

        if login_user:

            if login_user.is_active:

                if check_password(password, login_user.password):
                    print(username)
                    current_user['username']=login_user.username
                    current_user['password']=login_user.password
                    current_user['first_name']=login_user.first_name
                    current_user['last_name']=login_user.last_name
                    current_user['is_active']=True
                    current_user['comp_name']=login_user.comp_name
                    current_user['phone']=login_user.phone

                    request.session['admin'] = False
                    request.session['id'] = login_user.id
                    print(request.session.get('admin'))
                    return redirect('step1')

                else:
                    messages.info(request, 'The password entered was incorrect')
                    return render(request,'login.html')

            else:
                messages.info(request, 'Please confirm your email address to complete the registration')
                return redirect('login')

        else:
            messages.info(request, 'User not found')
            return redirect('login')

    else:
        user_all = User_Details.objects.all()
        return render(request,'login.html',{'obj': user_all})

def login_success(request):
    return render(request, 'login_success.html')

def login_verify(request):
    return render(request, 'login_verify.html')

def logout(request):
    try:
        del request.session['id']
        del request.session['admin']

    except KeyError:
        pass
    #print(request.session['id'])
    auth.logout(request)    
    return redirect('/')

def register(request):
    if request.method=='POST':
        print("Request method called")
        # print(json.loads(request.POST['data']))
        print("Without data worked below")
        print(request.POST)
        print(request.POST.get('first_name'))
        user1 = User_Details()
        user2 = Sandbox_Names()
        register_flag = True
        user1.first_name = request.POST.get('first_name')
        user1.last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        len_phone = len(phone)
        user1.phone = phone
        user1.username = request.POST.get('username')
        password = request.POST.get('password')
        len_pass = len(password)
        user1.password = make_password(password)
        c_password = request.POST.get('c_password')
        user1.comp_name = request.POST.get('comp_name')
        user1.user_img = 'default_avatar.png'

        try:
            new_user = User_Details.objects.raw('select * from  mywork_user_details')
        except:
            return render(request,'login.html')

        if len_phone != 10:
            register_flag = False
            return render(request, 'register.html', {'phone_error':'Enter a Valid Number', 'error':'Mobile Number Error'})

        for i in new_user:
            if user1.username in i.username:
                register_flag = False
                return render(request, 'register.html', {'email_error':'Type a new email', 'error': 'Email already exists'})

        if len_pass < 8:
            register_flag = False
            #messages.info(request, 'Password does not meet the requirement')
            return render(request, 'register.html', {'pass_error':'Password too short', 'error':'Password Error'})

        elif password != c_password:
            register_flag = False
            #messages.info(request, 'Password does not match')
            return render(request, 'register.html', {'c_pass_error':'Password does not match', 'error':'Password Error'})

        # r = RandomWords()
        try:
            #word1 = r.get_random_word(minLength=5, maxLength=5).lower()
            #word2 = r.get_random_word(minLength=5, maxLength=5).lower()
            url = urllib.request.urlopen(
            "https://raw.githubusercontent.com/sindresorhus/mnemonic-words/master/words.json")
            words = json.loads(url.read())
            random_word1 = random.choice(words)
            random_word2 = random.choice(words)
            code = "connect " + random_word1 + "-" + random_word2
        except:
            return HttpResponse("Server Unavailable")

        if register_flag:

            user2.username = user1.username
            user2.code = code
            user2.save()
            user1.save()
            user1.is_active = False;

            #s_user=User_Details.objects.raw('select * from mywork_user_details ')

            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            print("hello1")
            message = render_to_string('acc_active_email.html', {
            'user1': user1,
            'domain': current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(user1.pk)),
            # 'uid': force_bytes(user1.pk),
            'token':account_activation_token.make_token(user1),
            })
            print("hello2")

            to_email =  request.POST.get('username')
            print(to_email)
            send_mail(
            mail_subject,
            message,
            email_of_off,
            [to_email],
            fail_silently=False)
            #email = EmailMessage(mail_subject, message, to=[to_email])
            #email.send()
            messages.info(request, 'Please confirm your email address to complete the registration')
            return redirect('login_verify')

    else:
        return render(request, 'register.html')

def activate(request, uidb64, token):
    try:
        print("Activate Function Called")
        uid = force_text(urlsafe_base64_decode(uidb64))
        print("UID Printed Below")
        print(uid)
        print("token Printed Below")
        print(token)
        user2 = User_Details.objects.get(pk=uid)

    except(TypeError, ValueError, OverflowError, user2.DoesNotExist):
        user2 = None

    if user2 is not None and account_activation_token.check_token(user2, token):
        user2.is_active = True
        user2.save()

        return render(request, 'login_success.html', {'successful':'Thanking you for confirming your email.'})

    else:
        return render(request, 'login_success.html', {'successful':'Activation link is invalid.'})

def resend_link(request):
    if request.method=='POST':
        user1 = User_Details()

        username = request.POST.get('username')
        print(username)
        '''
        try:

            print(new_user)
        except:
            messages.info(request, 'User not found')
            return redirect('resend_link')
        '''

        new_user = User_Details.objects.filter(username=username)

        if not new_user:
            messages.info(request, 'User not found')
            return redirect('resend_link')

        for i in new_user:
            if username not in i.username:
                messages.info(request, 'User not found')
                return redirect('resend_link')

            else:
                with connection.cursor() as cursor:
                    sql_query = cursor.execute('select * from mywork_user_details where username=%s', [username])
                    sql_query_all = cursor.fetchall()

                for sql_query in sql_query_all:
                    print(sql_query)

                first_name = (sql_query[1])
                last_name = (sql_query[2])
                phone = (sql_query[3])
                password =  (sql_query[4])
                comp_name = (sql_query[6])
                is_active = (sql_query[7])
                user_img = (sql_query[8])
                #print(tuple_output)

                if is_active == 0:

                    user1.username = request.POST.get('username')
                    user1.phone = phone
                    user1.comp_name = comp_name
                    user1.password = password
                    user1.first_name = first_name
                    user1.last_name = last_name
                    user1.is_active = is_active
                    user1.user_img = user_img

                    with connection.cursor() as cursor:
                        #sql_query = cursor.execute('delete from mywork_user_details where username=%s', [username])
                        sql_query_id = cursor.execute('select id from mywork_user_details where username=%s', [username])
                        sql_query_all = cursor.fetchall()

                    for sql_query_id in sql_query_all:
                        print(sql_query_id)

                    user_id = (sql_query_id[0])

                    user1.id = user_id;
                    user1.save()

                    current_site = get_current_site(request)
                    mail_subject = 'Activate your account.'
                    message = render_to_string('acc_active_email.html', {
                    'user1': user1,
                    'domain': current_site.domain,
                    'uid':urlsafe_base64_encode(force_bytes(user1.pk)),
                    'token':account_activation_token.make_token(user1),
                    })

                    to_email = request.POST.get('username')
                    print(to_email)
                    send_mail(
                    mail_subject,
                    message,
                    email_of_off,
                    [to_email],
                    fail_silently=False)
                    #email = EmailMessage(mail_subject, message, to=[to_email])
                    #email.send()
                    messages.info(request, 'Please confirm your email address to complete the registration')
                    return redirect('login_verify')

                else:
                    messages.info(request, 'Email already verified')
                    return redirect('login')

    else:
        user_all = User_Details.objects.all()
        print(user_all)
        return render(request, 'resend_link.html', {'obj':user_all})

def forgot_password(request):

    if request.method=='POST':
        user1 = User_Details()

        username = request.POST.get('username')
        print(username)

        new_user = User_Details.objects.filter(username=username)

        if not new_user:
            messages.info(request, 'User not found')
            return redirect('forgot_password')

        for i in new_user:
            if username not in i.username:
                messages.info(request, 'User not found')
                return redirect('forgot_password')
            else:
                user1.save()
                current_site = get_current_site(request)
                mail_subject = 'Activate your account.'
                message = render_to_string('password_reset_email.html', {
                'user1': i.username,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user1.pk)),
                'token':account_activation_token.make_token(user1),
                })

                to_email = request.POST.get('username')
                print(to_email)
                send_mail(
                mail_subject,
                message,
                email_of_off,
                [to_email],
                fail_silently=False)
                #email = EmailMessage(mail_subject, message, to=[to_email])
                #email.send()
                return redirect('password_verify')

    else:
        return render(request, 'forgot_password.html')


def recover_password(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        print(uid)

    except:
        pass
        return render(request, 'login_success.html', {'successful':'Thanking you for confirming your email.'})

    else:
        return render(request, 'recover_password.html')

def password_reset_confirm(request):
    try:
        new_password = request.POST.get('password')
        confirm_password = request.POST.get('c_password')
        print(new_password, confirm_password)
        if new_password != confirm_password:
            return render(request, 'recover_password', {'error':'Passwords do not match'})
        else:
            user1 = User_Details()
            email = request.GET.get('email')


            print(email)

            return render(request, 'password_verify')

    except:
        return redirect('password_verify')

def password_verify(request):
    return render(request, 'password_verify.html')

def dashboard(request):
    response=""
    response1=""

    if request.session.get('id'):
        user_id = request.session.get('id')
        response += "User Id : {0} <br>".format(user_id)
        print(response)

    if request.session.get('admin') == False:
        admin_flag = request.session.get('admin')
        response1 += "Admin : {0}".format(admin_flag)
        print(response1)

    else:
        return render(request, 'index.html')

    if not response or not response1:
        return render(request, 'index.html')

    else:
        if admin_flag == False:
            user_disp = User_Details.objects.filter(id=request.session['id'])
            return render(request, 'dashboard.html', {'obj': user_disp})
        else:
            return render(request, 'index.html')


def sandbox(request):
    response=""
    response1=""

    if request.method == "POST":
        user1 = Sandbox_Webhook()

        user1.webhook = request.POST.get('user_webhook')
        user1.user_id = request.session['id']

        try:
            with connection.cursor() as cursor:
                sql_query_id = cursor.execute('select * from mywork_sandbox_webhook where user_id=%s',[user1.user_id])
                sql_query_all = cursor.fetchall()

            for sql_query_id in sql_query_all:
                print(sql_query_id)

            user = (sql_query_id[0])

            with connection.cursor() as cursor:
                cursor.execute('update mywork_sandbox_webhook set webhook=%s where user_id=%s',[user1.webhook, user1.user_id])

            messages.info(request, 'Your webhook has been updated successfully.')
            return redirect('sandbox')

        except:
            with connection.cursor() as cursor:
                sql_query_id_phone = cursor.execute('select phone from mywork_user_details where id=%s',[user1.user_id])
                sql_query_all_phone = cursor.fetchall()

            for sql_query_id_phone in sql_query_all_phone:
                print(sql_query_id_phone)

            user_phone = (sql_query_id_phone[0])
            print(user_phone)

            user1.phone = user_phone;
            user1.save()
            messages.info(request, 'Your webhook has been added successfully.')
            return redirect('sandbox')

    if request.session.get('id'):
        user_id = request.session.get('id')
        response += "User Id : {0} <br>".format(user_id)
        print(response)

    if request.session.get('admin') == False:
        admin_flag = request.session.get('admin')
        response1 += "Admin : {0}".format(admin_flag)
        print(response1)

    else:
        return render(request, 'index.html')

    if not response or not response1:
        return render(request, 'index.html')

    else:
        if admin_flag == False:
            user2 = Sandbox_Names()
            with connection.cursor() as cursor:
                #sql_query = cursor.execute('delete from mywork_user_details where username=%s', [username])
                sql_query_id = cursor.execute('select * from mywork_sandbox_names where id=%s', [request.session['id']])
                sql_query_all = cursor.fetchall()

            for sql_query_id in sql_query_all:
                print(sql_query_id[1])

            code_obj = Sandbox_Names.objects.filter(username=sql_query_id[1])
            user_disp = User_Details.objects.filter(id=request.session['id'])
            return render(request, 'sandbox.html', {'obj': code_obj, 'obj1': user_disp})

        else:
            return render(request, 'index.html')

def senders(request):
    response=""
    response1=""

    if request.session.get('id'):
        user_id = request.session.get('id')
        response += "User Id : {0} <br>".format(user_id)
        print(response)

    if request.session.get('admin') == False:
        admin_flag = request.session.get('admin')
        response1 += "Admin : {0}".format(admin_flag)
        print(response1)

    else:
        return render(request, 'login.html')

    if not response or not response1:
        return render(request, 'login.html')

    else:
        if admin_flag == False:
            businessprofile_obj = Business_Profile.objects.filter(user_id=request.session['id'])
            user_disp = User_Details.objects.filter(id=request.session['id'])
            return render(request, 'senders.html', {'obj': businessprofile_obj, 'obj1': user_disp})
        else:
            return render(request, 'login.html')


def senderno(request):
    response=""
    response1=""


    if request.GET.get('business_number'):
        print("Success")
        select_number_id = request.GET.get('business_number')
        print(select_number_id)

        '''
        with connection.cursor() as cursor:
            #sql_query = cursor.execute('delete from mywork_user_details where username=%s', [username])
            sql_query_id = cursor.execute('select * from mywork_user_details where select_number=%s', [select_number_id])
            sql_query_all = cursor.fetchall()

        for sql_query_id in sql_query_all:
            print(sql_query_id)
        '''
        if request.session.get('id'):
            print("Success 2")
            user_id = request.session.get('id')
            response += "User Id : {0} ".format(user_id)
            print(response)


        if request.session.get('admin') == False:
            admin_flag = request.session.get('admin')
            response1 += "Admin : {0}".format(admin_flag)
            print(response1)
        else:
            return render(request,'index.html')

        if not response or not response1:
            return render(request, 'index.html')


        if admin_flag == False:
            businessprofile_obj = Business_Profile.objects.filter(business_number=select_number_id)
            user_disp = User_Details.objects.filter(id=request.session.get('id'))
            print(businessprofile_obj)
            print(user_disp)
            return render(request, 'senderno.html', {'obj': businessprofile_obj, 'obj1': user_disp})
        else:
            return render(request,'index.html')


def configureno(request):
    response=""
    response1=""

    if request.session.get('id'):
        user_id = request.session.get('id')
        response += "User Id : {0} <br>".format(user_id)
        print(response)

    if request.session.get('admin') == False:
        admin_flag = request.session.get('admin')
        response1 += "Admin : {0}".format(admin_flag)
        print(response1)

    else:
        return render(request, 'index.html')

    if not response or not response1:
        return render(request, 'index.html')

    else:
        if admin_flag == False:
            user_disp = User_Details.objects.filter(id=request.session['id'])
            return render(request, 'configureno.html', {'obj': user_disp})
        else:
            return render(request, 'index.html')

def logs(request):
    response=""
    response1=""

    if request.session.get('id'):
        user_id = request.session.get('id')
        response += "User Id : {0} <br>".format(user_id)
        print(response)

    if request.session.get('admin') == False:
        admin_flag = request.session.get('admin')
        response1 += "Admin : {0}".format(admin_flag)
        print(response1)

    else:
        return render(request, 'index.html')

    if not response or not response1:
        return render(request, 'index.html')

    else:
        if admin_flag == False:
            user_disp = User_Details.objects.filter(id=request.session['id'])
            chats = user_message.objects.all().order_by('timestamp1')

            return render(request, 'logs.html', {'obj': chats, 'user':user_disp})
        else:
            return render(request, 'index.html')


# def send_template(request):
#     response=""
#     response1=""

#     if request.session.get('id'):
#         user_id = request.session.get('id')
#         response += "User Id : {0} <br>".format(user_id)
#         print(response)

#     if request.session.get('admin') == False:
#         admin_flag = request.session.get('admin')
#         response1 += "Admin : {0}".format(admin_flag)
#         print(response1)

#     else:
#         return render(request, 'index.html')

#     if not response or not response1:
#         return render(request, 'index.html')

#     else:
#         if admin_flag == False:
#             user_disp = User_Details.objects.filter(id=request.session['id'])
#             templates = template_master.objects.all()

#             return render(request, 'send_template.html', {'obj': templates, 'user': user_disp})
#         else:
#             return render(request, 'index.html')


def send_temp(request):
    if request.method == 'POST':
        #uploaded_file =
        t_name = request.POST.get('t_name', "")
        t_payload = request.POST.get('t_payload', "")
        
        numbers = ""
       # with open(, 'rt') as csvfile:
       # cfile=open(,'r')
        csv_file=request.FILES.get('t_file')
        file_data = csv_file.read().decode("utf-8")
        lines = file_data.split("\n")
        url = url_main + "/v1/users/login"
        payload = "{\n\t\"new_password\": \""+pass_for_api+"\"\n}"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic <base64(username:password)>',
            'Authorization': 'Basic ' + base_64 +"'"
        }
        response = requests.request("POST", url, headers=headers, data=payload, verify=False)
        rs = response.text
        json_data = json.loads(rs)
        authkey = json_data["users"][0]["token"]
        for line in lines:
            fields = line.split(",")
            to ="91"+fields[0].strip()
            if fields[0].strip() != "":
                payload = '{\n\t\"blocking": "wait",\n\t"contacts": [\n\t\t"'+fields[0].strip()+'"]\n}'

                headers = {
                    'Content-Type': "application/json",
                    'Authorization': "Bearer " + authkey,

                }
                response = requests.request("POST", url_main+"/v1/contacts", data=payload, headers=headers, verify=False)
                rs = response.text
                json_data = json.loads(rs)

                status = json_data["contacts"][0]["status"]
                payload = t_payload.replace("*91*",to)
                print(payload)
                if status == "valid":
                    headers = {
                        'Content-Type': "application/json",
                        'Authorization': "Bearer " + authkey,
                        'User-Agent': "PostmanRuntime/7.20.1",
                        'Accept': "*/*",
                        'Cache-Control': "no-cache",

                    }
                    response1 = requests.request("POST", url_main+"v1/messages", data=payload, headers=headers, verify=False)
                    rs = response1.text
                    json_data = json.loads(rs)
                    print(json_data)
                    message1 = user_message()
                    message1.wa_id = fields[0]
                    message1.message = payload
                    message1.name = ""
                    message1.m_type = 'template'
                    message1.m_from = 'website'
                    message1.timestamp1 = datetime.datetime.now()
                    message1.m_status = 'sent'
                    message1.m_service = "template"
                    message1.save()

                else:
                    message1 = user_message()
                    message1.wa_id = fields[0]
                    message1.message = payload
                    message1.name = ""
                    message1.m_type = 'template'
                    message1.m_from = 'website'
                    message1.timestamp1 = datetime.datetime.now()
                    message1.m_status = 'not sent'
                    message1.m_service = "template"
                    message1.save()
        return JsonResponse({"message": "success"}, status=200)


def getTemp(request):
    temp_id = request.POST.get('temp_id',"")
    temp = template_master.objects.filter(temp_id=temp_id).first()
    data = serializers.serialize("json",[temp])
    return JsonResponse({"data":data},status=200)


def insight1(request):
    response=""
    response1=""

    if request.session.get('id'):
        user_id = request.session.get('id')
        response += "User Id : {0} <br>".format(user_id)
        print(response)

    if request.session.get('admin') == False:
        admin_flag = request.session.get('admin')
        response1 += "Admin : {0}".format(admin_flag)
        print(response1)

    else:
        return render(request, 'index.html')

    if not response or not response1:
        return render(request, 'index.html')

    else:
        if admin_flag == False:
            user_disp = User_Details.objects.filter(id=request.session['id'])
            return render(request, 'insight1.html', {'obj': user_disp})
        else:
            return render(request, 'index.html')

def insight2(request):
    response=""
    response1=""

    if request.session.get('id'):
        user_id = request.session.get('id')
        response += "User Id : {0} <br>".format(user_id)
        print(response)

    if request.session.get('admin') == False:
        admin_flag = request.session.get('admin')
        response1 += "Admin : {0}".format(admin_flag)
        print(response1)

    else:
        return render(request, 'index.html')

    if not response or not response1:
        return render(request, 'index.html')

    else:
        if admin_flag == False:
            user_disp = User_Details.objects.filter(id=request.session['id'])
            return render(request, 'insight2.html', {'obj': user_disp})
        else:
            return render(request, 'index.html')

def usage(request):
    response=""
    response1=""

    if request.session.get('id'):
        user_id = request.session.get('id')
        response += "User Id : {0} <br>".format(user_id)
        print(response)

    if request.session.get('admin') == False:
        admin_flag = request.session.get('admin')
        response1 += "Admin : {0}".format(admin_flag)
        print(response1)

    else:
        return render(request, 'index.html')

    if not response or not response1:
        return render(request, 'index.html')

    else:
        if admin_flag == False:
            user_disp = User_Details.objects.filter(id=request.session['id'])
            return render(request, 'usage.html', {'obj': user_disp})
        else:
            return render(request, 'index.html')

def viewuse(request):
    response=""
    response1=""

    if request.session.get('id'):
        user_id = request.session.get('id')
        response += "User Id : {0} <br>".format(user_id)
        print(response)

    if request.session.get('admin') == False:
        admin_flag = request.session.get('admin')
        response1 += "Admin : {0}".format(admin_flag)
        print(response1)

    else:
        return render(request, 'index.html')

    if not response or not response1:
        return render(request, 'index.html')

    else:
        if admin_flag == False:
            user_disp = User_Details.objects.filter(id=request.session['id'])
            return render(request, 'viewuse.html', {'obj': user_disp})
        else:
            return render(request, 'index.html')

def general_settings(request):
    response=""
    response1=""

    if request.session.get('id'):
        user_id = request.session.get('id')
        response += "User Id : {0} <br>".format(user_id)
        print(response)

    if request.session.get('admin') == False:
        admin_flag = request.session.get('admin')
        response1 += "Admin : {0}".format(admin_flag)
        print(response1)

    else:
        return render(request, 'index.html')

    if not response or not response1:
        return render(request, 'index.html')

    else:
        if admin_flag == False:
            user_disp = User_Details.objects.filter(id=request.session['id'])
            return render(request, 'general_settings.html', {'obj': user_disp})
        else:
            return render(request, 'index.html')

def businessprofile(request):
    response = ""
    response1=""

    if request.method=='POST':
        user1 = Business_Profile()

        user1.Comp_name = request.POST.get('Comp_name')
        user1.Business_desc = request.POST.get('Business_desc')
        user1.Business_Category = request.POST.get('Business_Category')
        user1.facebook_id = request.POST.get('facebook_id')
        user1.business_disp_name = request.POST.get('business_disp_name')
        user1.about_business = request.POST.get('about_business')
        user1.business_address = request.POST.get('business_address')
        user1.business_email = request.POST.get('business_email')
        user1.business_number = request.POST.get('business_number')
        user1.radio = request.POST.get('radio')
        user1.website = request.POST.get('website')
        user1.user_id = request.session['id']


        # print(request.session['id'])

        try:
            new_select_number = Business_Profile.objects.raw('select * from  mywork_business_profile')
        except:
            return render(request,'businessprofile.html')

        for i in new_select_number:
            if user1.business_number in i.business_number:
               return render(request, 'businessprofile.html', {'num_error': 'Number already exists.'})


        # len_select_number = len(user1.business_number)
        # if len_select_number != 12:
        #     return render(request, 'businessprofile.html', {'num_len_error': 'Number should be 10 digit with your country code'})


        #user1.user_id = request.session['id']
        user1.save()


        current_site = get_current_site(request)
        mail_subject = 'Registration Pending'
        message = render_to_string('businessprofile_msg.html', {
        'comp_name':user1.Comp_name,
        'number': user1.business_number,
        'display_name': user1.business_disp_name,
        'facebook_id': user1.facebook_id,
        'comp_addr': user1.business_address,
        'comp_email': user1.business_email,
        'website': user1.website,
        
        })
        print(user1.business_email,message)
        send_mail(
        mail_subject,
        message,
        'noreply@kwiqreply.io',
        [user1.business_email],
        fail_silently=False)

        messages.info(request, 'Your form has been successfully submitted')
        return redirect('senders')

    else:
        if request.session.get('id'):
            user_id = request.session.get('id')
            response += "User Id : {0} <br>".format(user_id)
            print(response)

        if request.session.get('admin') == False:
            admin_flag = request.session.get('admin')
            response1 += "Admin : {0}".format(admin_flag)
            print(response1)

        else:
            return render(request, 'index.html')

        if not response or not response1:
            return render(request, 'index.html')

        else:
            if admin_flag == False:
                print(request.session.get('id'))
                user_disp = User_Details.objects.filter(id=request.session.get('id'))
                return render(request, 'businessprofile.html', {'obj': user_disp})
            else:
                return render(request, 'index.html')

def profile(request):
    response=""
    response1=""
    user_obj = User_Details.objects.filter(id=request.session['id'])

    if request.method=='POST':
        user1 = User_Details()
        print(user1.first_name)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        #username = request.POST.get('username')
        phone = request.POST.get('phone')
        comp_name = request.POST.get('comp_name')
        user_id = request.session.get('id')

        try:
            uploaded_file = request.FILES['document']

            with connection.cursor() as cursor:
                #sql_query = cursor.execute('delete from mywork_user_details where username=%s', [username])
                sql_query_id = cursor.execute('select user_img from mywork_user_details where id=%s', [user_id])
                sql_query_all = cursor.fetchall()

            for sql_query_id in sql_query_all:
                print(sql_query_id[0])

            if uploaded_file.content_type == 'image/jpeg' or uploaded_file.content_type == 'image/png' :
                with connection.cursor() as cursor:
                    # if sql_query_id[0] != "default_avatar.png":
                    #     os.remove(os.path.join(settings.MEDIA_ROOT, sql_query_id[0]))
                    file_name = uuid.uuid4().hex
                    file_storage = FileSystemStorage()
                    file_storage.save(file_name, uploaded_file)
                    #os.rename(uploaded_file.name, "{id}{uuid}".format(id=user_id, uuid=file_name))
                    cursor.execute('update mywork_user_details set user_img=%s where id=%s', [file_name,user_id])

            else:
                return render(request, 'profile.html', {'img_content':'Please upload a JPEG/PNG image type.', 'obj':user_obj})

        except:
            pass

        try:
            if phone is not None:
                len_phone = len(phone)
                print(len)
                if len_phone == 10:
                    with connection.cursor() as cursor:
                        sql_query = cursor.execute('update mywork_user_details set first_name=%s, last_name=%s,  phone=%s, comp_name=%s where id=%s', [first_name, last_name,phone, comp_name, user_id])
                    return render(request, 'profile.html', {'profile_update':'Profile updated successfully.', 'obj':user_obj})
                else:
                    return render(request, 'profile.html', {'phone_error_len':'Please enter 10 digit number.', 'obj':user_obj})
        except:
            pass

        update_user = User_Details.objects.raw('select * from mywork_user_details where id=%s',[user_id])[0]
        curr_pass = request.POST.get('current_password')
        up_password = request.POST.get('password')
        len_pass = len(up_password)
        confrim_password = request.POST.get('confirm_password')

        try:
            if curr_pass is not None:

                if check_password(curr_pass, update_user.password):

                    if curr_pass != up_password:

                        if up_password == confrim_password:

                            if len_pass >= 8:

                                if up_password == confrim_password:
                                    up_password = make_password(up_password)
                                    with connection.cursor() as cursor:
                                        sql_query = cursor.execute('update mywork_user_details set password=%s where id=%s',[up_password, user_id])
                                    return render(request, 'profile.html', {'success_update':'Password has been successfully changed.', 'obj':user_obj})

                            else:
                                return render(request, 'profile.html', {'min_error':'Password should be minimum 8 characters.', 'obj':user_obj})

                        else:
                            return render(request, 'profile.html', {'diff_pass':'Please make sure the entered passwords match.', 'obj':user_obj})

                    else:
                        return render(request, 'profile.html', {'old_new_error':'Old password matches the new password.', 'obj':user_obj})

                else:
                    return render(request, 'profile.html', {'curr_error':'Current password entered is incorrect.', 'obj':user_obj})

        except:
            pass

    if request.session.get('id'):
        user_id = request.session.get('id')
        response += "User Id : {0}".format(user_id)
        print(response)

    if request.session.get('admin') == False:
        admin_flag = request.session.get('admin')
        response1 += "Admin : {0}".format(admin_flag)
        print(response1)

    else:
        return render(request, 'index.html')

    if not response or not response1:
        return render(request, 'index.html')

    else:
        if admin_flag == False:
            user_disp = User_Details.objects.filter(id=request.session['id'])
            return render(request, 'profile.html', {'obj':user_obj, 'obj1':user_disp})
        else:
            return render(request, 'index.html')


def support(request):
    response=""
    response1=""

    if request.session.get('id'):
        user_id = request.session.get('id')
        response += "User Id : {0} <br>".format(user_id)
        print(response)

    if request.session.get('id'):
        user_id = request.session.get('id')
        response += "User Id : {0}".format(user_id)
        print(response)

    if request.session.get('admin') == False:
        admin_flag = request.session.get('admin')
        response1 += "Admin : {0}".format(admin_flag)
        print(response1)

    else:
        return render(request, 'index.html')

    if not response or not response1:
        return render(request, 'index.html')

    else:
        if admin_flag == False:
            user_disp = User_Details.objects.filter(id=request.session['id'])
            return render(request, 'support.html', {'obj': user_disp})
        else:
            return render(request, 'index.html')

def submit_ticket(request):
    if request.method=='POST':
        user1 = Submit_Ticket()

        user1.subject = request.POST.get('subject')
        user1.comment = request.POST.get('comment')
        user1.product = request.POST.get('product')
        user1.business_impact = request.POST.get('business_impact')
        user1.ticketdate = date.today()
        user1.user_id = request.session['id']

        user1.save()

        current_site = get_current_site(request)
        mail_subject = 'Ticket is submitted'
        message = render_to_string('submit_ticket_msg.html', {
        'subject': user1.subject,
        'comment': user1.comment,
        'product': user1.product,
        'business_impact': user1.business_impact,
        })

        send_mail(
        mail_subject,
        message,
        email_of_off,
        ['kkarnik22@gmail.com'],
        fail_silently=False)

        messages.info(request, 'Your form has been successfully submitted')
        return redirect('support')

    else:
        response=""
        response1=""

        if request.session.get('id'):
            user_id = request.session.get('id')
            response += "User Id : {0} <br>".format(user_id)
            print(response)

        if request.session.get('admin') == False:
            admin_flag = request.session.get('admin')
            response1 += "Admin : {0}".format(admin_flag)
            print(response1)

        else:
            return render(request, 'index.html')

        if not response or not response1:
            return render(request, 'index.html')

        else:
            if admin_flag == False:
                user_disp = User_Details.objects.filter(id=request.session['id'])
                return render(request, 'submit_ticket.html', {'obj': user_disp})
            else:
                return render(request, 'index.html')

def ticket_history(request):
    response=""
    response1=""
    if request.session.get('id'):
        user_id = request.session.get('id')
        response += "User Id : {0} <br>".format(user_id)
        print(response)

    if request.session.get('admin') == False:
        admin_flag = request.session.get('admin')
        response1 += "Admin : {0}".format(admin_flag)
        print(response1)

    else:
        return render(request, 'index.html')

    if not response or not response1:
        return render(request, 'index.html')

    else:
        if admin_flag == False:
            user_disp = User_Details.objects.filter(id=request.session['id'])
            ticket_obj = Submit_Ticket.objects.filter(user_id=request.session['id'])
            return render(request, 'ticket_history.html', {'obj': user_disp, 'obj1':ticket_obj})
        else:
            return render(request, 'index.html')

def chat_window(request):
    response=""
    response1=""

    if request.session.get('id'):
        user_id = request.session.get('id')
        response += "User Id : {0} <br>".format(user_id)
        print(response)

    if request.session.get('admin') == False:
        admin_flag = request.session.get('admin')
        response1 += "Admin : {0}".format(admin_flag)
        print(response1)

    else:
        return render(request, 'index.html')

    if not response or not response1:
        return render(request, 'index.html')

    else:
        if admin_flag == False:
            user_disp = User_Details.objects.filter(id=request.session['id'])
            return render(request, 'chat_window.html', {'obj': user_disp})

        else:
            return render(request, 'index.html')

def sales(request):
    if request.method=='POST':

        user1 = Sales()
        print("hello")
        user1.name = request.POST.get('name')
        user1.email = request.POST.get('email')
        user1.comp_name = request.POST.get('comp_name')
        user1.job = request.POST.get('job')
        user1.phone_number = request.POST.get('phone_number')
        user1.country = request.POST.get('country')
        user1.state = request.POST.get('state')
        user1.user_id = request.session['id']

        len_phone_number = len(user1.phone_number)
        if len_phone_number != 10:
            return render(request, 'sales.html', {'error': 'Number should be 10 digit.'})

        user1.save()

        current_site = get_current_site(request)
        mail_subject = 'Sales Enquiry'
        message = render_to_string('sales_msg.html', {
        'name': user1.name,
        'email': user1.email,
        'comp_name': user1.comp_name,
        'job': user1.job,
        'phone_number': user1.phone_number,
        'country': user1.country,
        'state': user1.state,
        })

        send_mail(
        mail_subject,
        message,
        email_of_off,
        ['jsmith.sg6@gmail.com'],
        fail_silently=False)

        messages.info(request, 'Your form has been successfully submitted')
        return redirect('support')

    else:
        response=""
        response1=""

        if request.session.get('id'):
            user_id = request.session.get('id')
            response += "User Id : {0} <br>".format(user_id)
            print(response)

        if request.session.get('admin') == False:
            admin_flag = request.session.get('admin')
            response1 += "Admin : {0}".format(admin_flag)
            print(response1)

        else:
            return render(request, 'index.html')

        if not response or not response1:
            return render(request, 'index.html')

        else:
            if admin_flag == False:
                user_disp = User_Details.objects.filter(id=request.session['id'])
                return render(request, 'sales.html', {'obj': user_disp})

            else:
                return render(request, 'index.html')

def step1(request):
    response=""
    response1=""

    if request.session.get('id'):
        user_id = request.session.get('id')
        response += "User Id : {0} <br>".format(user_id)
        print(response)

    if request.session.get('admin') == False:
        admin_flag = request.session.get('admin')
        response1 += "Admin : {0}".format(admin_flag)
        print(response1)

    else:
        return render(request, 'index.html')

    if not response or not response1:
        return render(request, 'index.html')

    else:
        if admin_flag == False:
            # while True:
            #     if check_message() == 0:
            #     print("0")
            #     break
            user_disp = User_Details.objects.filter(id=request.session['id'])
            return render(request, 'step1.html', {'obj': user_disp})
        else:
            return render(request, 'index.html')

def step2(request):
    response=""
    response1=""

    if request.session.get('id'):
        user_id = request.session.get('id')
        response += "User Id : {0} <br>".format(user_id)
        print(response)

    if request.session.get('admin') == False:
        admin_flag = request.session.get('admin')
        response1 += "Admin : {0}".format(admin_flag)
        print(response1)

    else:
        return render(request, 'index.html')

    if not response or not response1:
        return render(request, 'index.html')

    else:
        if admin_flag == False:
            user_disp = User_Details.objects.filter(id=request.session['id'])
            return render(request, 'step2.html', {'obj': user_disp})
        else:
            return render(request, 'index.html')

def step3(request):
    response=""
    response1=""

    if request.session.get('id'):
        user_id = request.session.get('id')
        response += "User Id : {0} <br>".format(user_id)
        print(response)

    if request.session.get('admin') == False:
        admin_flag = request.session.get('admin')
        response1 += "Admin : {0}".format(admin_flag)
        print(response1)

    else:
        return render(request, 'index.html')

    if not response or not response1:
        return render(request, 'index.html')

    else:
        if admin_flag == False:
            user_disp = User_Details.objects.filter(id=request.session['id'])
            return render(request, 'step3.html', {'obj': user_disp})
        else:
            return render(request, 'index.html')

def step4(request):
    response=""
    response1=""

    if request.session.get('id'):
        user_id = request.session.get('id')
        response += "User Id : {0} <br>".format(user_id)
        print(response)

    if request.session.get('admin') == False:
        admin_flag = request.session.get('admin')
        response1 += "Admin : {0}".format(admin_flag)
        print(response1)

    else:
        return render(request, 'index.html')

    if not response or not response1:
        return render(request, 'index.html')

    else:
        if admin_flag == False:
            user_disp = User_Details.objects.filter(id=request.session['id'])
            return render(request, 'step4.html', {'obj': user_disp})
        else:
            return render(request, 'index.html')

def step5(request):
    response=""
    response1=""

    if request.session.get('id'):
        user_id = request.session.get('id')
        response += "User Id : {0} <br>".format(user_id)
        print(response)

    if request.session.get('admin') == False:
        admin_flag = request.session.get('admin')
        response1 += "Admin : {0}".format(admin_flag)
        print(response1)

    else:
        return render(request, 'index.html')

    if not response or not response1:
        return render(request, 'index.html')

    else:
        if admin_flag == False:
            user_disp = User_Details.objects.filter(id=request.session['id'])
            return render(request, 'step5.html', {'obj': user_disp})
        else:
            return render(request, 'index.html')


def converse(request):

    response=""
    response1=""

    if request.session.get('id'):
        user_id = request.session.get('id')
        response += "User Id : {0} <br>".format(user_id)
        print(response)

    if request.session.get('admin') == False:
        admin_flag = request.session.get('admin')
        response1 += "Admin : {0}".format(admin_flag)
        print(response1)

    else:
        return render(request, 'index.html')

   # if not response or not response1:
     #   return render(request, 'index.html')

   # else:
         #message_details = user_message.objects.raw('select * from mywork_user_message')
        # message_requests = user_message.objects.raw('SELECT id ,name,wa_id as number,(SELECT COUNT(*)  FROM mywork_user_message where m_status=%s AND wa_id=number) as no_of_messages  from mywork_user_message GROUP BY wa_id order by timestamp1 asc',['unread'])

    if admin_flag == False:
        user_disp = User_Details.objects.filter(id=request.session['id'])
        return render(request, 'converse.html', {'obj': user_disp})
    else:
        return render(request, 'index.html')


def chat_statistics(request):
    response=""
    response1=""

    if request.session.get('id'):
        user_id = request.session.get('id')
        response += "User Id : {0} <br>".format(user_id)
        print(response)

    if request.session.get('admin') == False:
        admin_flag = request.session.get('admin')
        response1 += "Admin : {0}".format(admin_flag)
        print(response1)

    else:
        return render(request, 'index.html')

    if not response or not response1:
        return render(request, 'index.html')

    else:
        if admin_flag == False:
            user_disp = User_Details.objects.filter(id=request.session['id'])
            return render(request, 'chat_statistics.html', {'obj': user_disp})
        else:
            return render(request, 'index.html')


def audience(request):
    response=""
    response1=""

    if request.session.get('id'):
        user_id = request.session.get('id')
        response += "User Id : {0} <br>".format(user_id)
        print(response)

    if request.session.get('admin') == False:
        admin_flag = request.session.get('admin')
        response1 += "Admin : {0}".format(admin_flag)
        print(response1)

    else:
        return render(request, 'index.html')

    if not response or not response1:
        return render(request, 'index.html')

    else:
        if admin_flag == False:
            user_disp = User_Details.objects.filter(id=request.session['id'])
            return render(request, 'audience.html', {'obj': user_disp})
        else:
            return render(request, 'index.html')


def announce(request):
    response=""
    response1=""

    if request.session.get('id'):
        user_id = request.session.get('id')
        response += "User Id : {0} <br>".format(user_id)
        print(response)

    if request.session.get('admin') == False:
        admin_flag = request.session.get('admin')
        response1 += "Admin : {0}".format(admin_flag)
        print(response1)

    else:
        return render(request, 'index.html')

    if not response or not response1:
        return render(request, 'index.html')

    else:
        if admin_flag == False:
            user_disp = User_Details.objects.filter(id=request.session['id'])
            return render(request, 'announce.html', {'obj': user_disp})
        else:
            return render(request, 'index.html')


def create_new_ant(request):
    response=""
    response1=""

    if request.session.get('id'):
        user_id = request.session.get('id')
        response += "User Id : {0} <br>".format(user_id)
        print(response)

    if request.session.get('admin') == False:
        admin_flag = request.session.get('admin')
        response1 += "Admin : {0}".format(admin_flag)
        print(response1)

    else:
        return render(request, 'index.html')

    if not response or not response1:
        return render(request, 'index.html')

    else:
        if admin_flag == False:
            user_disp = User_Details.objects.filter(id=request.session['id'])
            return render(request, 'create_new_ant.html', {'obj': user_disp})
        else:
            return render(request, 'index.html')


def session_manage(request):
    response=""
    response1=""

    if request.session.get('id'):
        user_id = request.session.get('id')
        response += "User Id : {0} <br>".format(user_id)
        print(response)

    if request.session.get('admin') == False:
        admin_flag = request.session.get('admin')
        response1 += "Admin : {0}".format(admin_flag)
        print(response1)

    else:
        return render(request, 'index.html')

    if not response or not response1:
        return render(request, 'index.html')

    else:
        if admin_flag == False:
            user_disp = User_Details.objects.filter(id=request.session['id'])
            return render(request, 'session_manage.html', {'obj': user_disp})
        else:
            return render(request, 'index.html')


def post_session(request):
    response=""
    response1=""

    if request.session.get('id'):
        user_id = request.session.get('id')
        response += "User Id : {0} <br>".format(user_id)
        print(response)

    if request.session.get('admin') == False:
        admin_flag = request.session.get('admin')
        response1 += "Admin : {0}".format(admin_flag)
        print(response1)

    else:
        return render(request, 'index.html')

    if not response or not response1:
        return render(request, 'index.html')

    else:
        if admin_flag == False:
            user_disp = User_Details.objects.filter(id=request.session['id'])
            return render(request, 'post_session.html', {'obj': user_disp})
        else:
            return render(request, 'index.html')


def notification_api(request):
    response=""
    response1=""

    if request.session.get('id'):
        user_id = request.session.get('id')
        response += "User Id : {0} <br>".format(user_id)
        print(response)

    if request.session.get('admin') == False:
        admin_flag = request.session.get('admin')
        response1 += "Admin : {0}".format(admin_flag)
        print(response1)

    else:
        return render(request, 'index.html')

    if not response or not response1:
        return render(request, 'index.html')

    else:
        if admin_flag == False:
            user_disp = User_Details.objects.filter(id=request.session['id'])
            return render(request, 'notification_api.html', {'obj': user_disp})
        else:
            return render(request, 'index.html')

def clean_body(msg):    
    new = []
    su = ""

    for i in msg:
        if i == '\"':
            i = i.replace(i,'\\"')
        elif i == '\\':
            i = i.replace(i, '\\\\')
        # elif i == '\n':
        #     i = i.replace(i, '\\\\n')

        else:
            pass
        new += i

    for x in new:
        su += x

    return su


def send_message(request):
    
    msg = str(request.GET.get('message', None))
    to = str(request.GET.get('to', None))
    name = request.GET.get('name', None)
    # print(msg)
    # body = "i"
    print(msg)
    body = str(clean_body(msg).encode('UTF_8'))

    print("to : " + to + " name : " + name + " body : "+ body[2:-1])

    authkey= update_authkey()
    # print(authkey)
    
    url = url_main + "/v1/messages"
    # print("to = {}this si braces {}one   ".format(to,body))
    # payload = '''{"to": "{}","type": "text","recipient_type": "individual","text": { "body": "{}" }  \}'''.format(to,msg)
    # print("Payload Below")
    # print(payload)
    payload = "{\n  \"to\": \"" + str(to) + "\",\n  \"type\": \"text\",\n  \"recipient_type\": \"individual\",\n  \"text\": {\n    \"body\": \"" + str(body[2:-1]) + "\"\n  }\n}\n"
    # print(type(payload.encode('UTF-8')))
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer " + authkey,
    }

    
        # return HttpResponse(resp)

    try:
        resp = requests.request("POST", url, data=payload, headers=headers, verify=False)
        
        rs = json.loads(resp.text)      
        print(rs)
        msg_id = rs["messages"][0]["id"]
        
        if body!="":
            # resp = requests.request("POST", url.rstrip(), data=payload, headers=headers, verify=False)
            message1=user_message()
            message1.wa_id=to
            body = body.replace('\\n','<br>')
            message1.message=body[2:-1]
            message1.name=name
            message1.m_type='text'
            message1.m_from='website'
            # message1.timestamp1=datetime.datetime.now()
            message1.timestamp1=timezone.now()
            print(timezone.now())
            message1.m_status='unread'
            message1.unique_msg_id = msg_id
            message1.save()
            print("record Inserted in db")


        
        return JsonResponse({'status':'success'})

    except Exception as e:
        print(e)
        print("Exception printd")
        return JsonResponse({'status':'Error'})
    # return HttpResponse(resp)



def get_chat(request):
    response = ""
    response1 = ""
    wa_number = request.GET.get('wa_number', None)
    id = request.session.get('id')
    # chats = user_message.objects.filter(wa_id=wa_number)
    # for chat in chats:
    #     if chat.m_media != '':
    #         url = url_main + "/v1/users/login"
    #         payload = "{\n\t\"new_password\": \""+pass_for_api+"\"\n}"
    #         headers = {
    #             'Content-Type': 'application/json',
    #             'Authorization': 'Basic <base64(username:password)>',
    #             'Authorization': 'Basic ' + base_64 +"'"
    #         }
    #         response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    #         rs = response.text
    #         print(rs)
    #         json_data = json.loads(rs)
    #         authkey = json_data["users"][0]["token"]

    #         url = url_main + "/v1/media/" + chat.m_media

    #         headers = {
    #             'Content-Type': "application/json",
    #             'Authorization': "Bearer " + authkey,
    #             'cache-control': "no-cache",
    #             'Postman-Token': "c7225772-08c7-43f8-b905-1b18da80d814"
    #         }
    #         response1 = requests.request("GET", url, headers=headers, verify=False)
    #         image = response1.content
    #         encoded_data = base64.b64encode(image)
    #         ts = int(time.time())
    #         file1 = ""
    #         m_url = ""
    #         ext = ""

    #         if chat.m_type == 'image':
    #             m_url = "media/image/"
    #             ext = chat.m_url
    #             ext = ext.split("/", 1)[1]
    #             file1 = 'image_' + str(ts) + "." + "jpg"
    #             fh = open(os.path.join(settings.MEDIA_ROOT + "/image/", file1), "wb")
    #             fh.write(base64.decodebytes(encoded_data))
    #             fh.close()

    #         elif chat.m_type == 'video':
    #             m_url = 'media/video/'
    #             ext = chat.m_url
    #             ext = ext.split("/", 1)[1]
    #             file1 = 'video_' + str(ts) + "." + "mp4"
    #             fh = open(os.path.join(settings.MEDIA_ROOT + '/video/', file1), "wb")
    #             fh.write(base64.decodebytes(encoded_data))
    #             fh.close()
    #         elif chat.m_type == 'documents':
    #             m_url = 'media/documents/'
    #             ext = chat.m_url
    #             ext = ext.split("/", 1)[1]
    #             file1 = chat.m_fileName
    #             # file1 = 'document_' + str(ts) + "." + "pdf"
    #             fh = open(os.path.join(settings.MEDIA_ROOT + '/documents/', file1), "wb")
    #             fh.write(base64.decodebytes(encoded_data))
    #             fh.close()
    #         user_message.objects.filter(id=chat.id).update(m_url=m_url, m_fileName=file1, m_media='')
    chats = user_message.objects.filter(wa_id=wa_number)
    user_message.objects.filter(wa_id=wa_number).update(m_status='read')

    # print(id)
    # print("ID PRINTEC ABOVW")

    user_detail = User_Details.objects.filter(id = id)
    
    return render(request, 'chat.html', {'obj': chats,'user_detail_model' : user_detail})


def get_unread(request):

    wa_number = request.GET.get('wa_number', None)
    # chat1 = user_message.objects.raw('select * from mywork_user_message where wa_id=%s and m_status=%s ORDER BY '
    #                                  'timestamp1', [wa_number, 'unread'])
    # for chat in chat1:
    #     if chat.m_media != '':
    #         url = url_main + "/v1/users/login"
    #         payload = "{\n\t\"new_password\": \""+pass_for_api+"\"\n}"
    #         headers = {
    #             'Content-Type': 'application/json',
    #             'Authorization': 'Basic <base64(username:password)>',
    #             'Authorization': 'Basic '+base_64 + "'"
    #         }
    #         response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    #         rs = response.text
    #         json_data = json.loads(rs)
    #         authkey = json_data["users"][0]["token"]
    #         url = url_main + "/v1/media/" + chat.m_media

    #         headers = {
    #             'Content-Type': "application/json",
    #             'Authorization': "Bearer " + authkey,
    #             'cache-control': "no-cache",
    #             'Postman-Token': "c7225772-08c7-43f8-b905-1b18da80d814"
    #         }
    #         response1 = requests.request("GET", url, headers=headers, verify=False)
    #         image = response1.content
    #         encoded_data = base64.b64encode(image)
    #         ts = int(time.time())
    #         file1 = ""
    #         m_url = ""
    #         ext = ""

    #         if chat.m_type == 'image':
    #             m_url = 'media/image/'
    #             ext = chat.m_url
    #             ext = ext.split("/", 1)[1]
    #             file1 = 'image_' + str(ts) + "." + "jpg"
    #             fh = open(os.path.join(settings.MEDIA_ROOT + "/image/", file1), "wb")
    #             fh.write(base64.decodebytes(encoded_data))
    #             fh.close()
    #         elif chat.m_type == 'video':
    #             m_url = 'media/video/'
    #             ext = chat.m_url
    #             ext = ext.split("/", 1)[1]
    #             file1 = 'video_' + str(ts) + "." + "mp4"
    #             fh = open(os.path.join(settings.MEDIA_ROOT + '/video/', file1), "wb")
    #             fh.write(base64.decodebytes(encoded_data))
    #             fh.close()
    #         elif chat.m_type == 'document':
                
    #             m_url = 'media/documents/'
    #             ext = chat.m_url
    #             ext = ext.split("/", 1)[1]
    #             file1 = chat.m_fileName
    #             fh = open(os.path.join(settings.MEDIA_ROOT + '/documents/', file1), "wb")
    #             fh.write(base64.decodebytes(encoded_data))
    #             fh.close()
    #         user_message.objects.filter(id=chat.id).update(m_url=m_url, m_fileName=file1, m_media='')

    chat1 = user_message.objects.raw(
                'select * from mywork_user_message where wa_id=%s and m_status=%s ORDER BY '
                'timestamp1', [wa_number, 'unread'])
    
    # chat1 = user_message.objects.filter(wa_id = wa_number,m_status = 'unread' )  
    
    return render(request, 'chat.html', {'obj': chat1})


def update_status(request):
    wa_number = request.GET.get('wa_number', None)
    ac = user_message.objects.filter(wa_id=wa_number).filter(m_status="unread").update(m_status="read")
    return HttpResponse(status=200)


def get_count(request):
    message_requests = user_message.objects.raw('SELECT id,name,wa_id as number,(SELECT COUNT(*)  FROM '
                                                'mywork_user_message where m_status=%s AND wa_id=number) as '
                                                'no_of_messages  from mywork_user_message GROUP BY wa_id order by '
                                                'timestamp1 DESC', ['unread'])
    

    # message_requests = user_message.objects.values('id','name',number = 'wa_id',co=Subquery(user_message.objects.filter(m_status = 'unread').count())).filter(m_status = 'unread').order_by('-timestamp1')
    # print(message_requests.query)
    return render(request, 'get_count.html', {'obj2': message_requests})


def search(request):
    searchTerm = request.GET.get('search', None)
    searchTerm = '%'+searchTerm+'%'
    message_requests = user_message.objects.raw('SELECT id,name,wa_id as number '
                                                'from mywork_user_message where wa_id LIKE %s GROUP BY wa_id', [searchTerm])

    return render(request, 'get_count.html', {'obj2': message_requests})


def send_file(request):
    print("Request below")
    print(request.FILES)
    if request.method == 'POST':
        if "browseFile" in request.FILES:
            uploaded_file = request.FILES['browseFile']

        else:
            uploaded_file = ""
        caption = request.POST.get('caption', "")
        to = request.POST.get('to', "")
        name = request.POST.get('name', "")
        link = request.POST.get('load', "")
        # print()
        # sys.exit(uploaded_file.content_type)

        if link != "":

            #url = "https://waent-lb-387296617.ap-southeast-1.elb.amazonaws.com" + "/v1/users/login"
            url = url_main + "/v1/users/login"
            payload = "{\n\t\"new_password\": \""+pass_for_api+"\"\n}"
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Basic <base64(username:password)>',
                'Authorization': 'Basic ' + base_64 + "'"
            }
            response = requests.request("POST", url, headers=headers, data=payload, verify=False)
            rs = response.text
            json_data = json.loads(rs)
            authkey = json_data["users"][0]["token"]
            response = requests.get(link)
            content_type = mimetypes.guess_type(link)
            a = urlparse(link)
            print(a.path)
            filename = os.path.basename(a.path)
            # print(content_type)
            type1 = ""
            payload1 = ""
            if "image" in str(content_type):
                type1 = 'image'
                payload1 = "{\n\t\"to\": \"" + to + "\",\n\t\"type\": \"" + type1 + "\",\n\t\"recipient_type\": \"individual\",\n\t\"image\": {\n\t\t\"link\": \"" + link + "\",\n\t\t\"caption\": \"" + caption + "\"\n\t}\n}\n"
            elif "video" in str(content_type):
                type1 = 'video'
                payload1 = "{\n\t\"to\": \"" + to + "\",\n\t\"type\": \"" + type1 + "\",\n\t\"recipient_type\": \"individual\",\n\t\"video\": {\n\t\t\"link\": \"" + link + "\",\n\t\t\"caption\": \"" + caption + "\"\n\t}\n}\n"
            else:
                print("in")
                type1 = 'document'
                payload1 = "{\n\t\"to\": \"" + to + "\",\n\t\"type\": \"document\",\n\t\"recipient_type\": \"individual\",\n\t\"document\": {\n\t\t\t\"caption\": \"" + caption + "\",\n\t\t\"link\": \"" + link + "\",\n\t\t\"filename\": \"" + filename + "\"\n\t}\n}\n"

            url = url_main + "/v1/messages/"
            # print(payload1)
            # payload1 = "{\n\t\"to\": \"" + to + "\", \n\t\"type\": \"image\", \n\t\"recipient_type\": \"individual\", \n\t\"image\": {\n\t\t\"id\": \"" + img_id + "\",\n\t\t\t\"caption\": \"" + caption + "\"\n\t\t}\n}\n"
            headers = {
                'Content-Type': "application/json",
                'Authorization': "Bearer " + authkey,
                'cache-control': "no-cache"

            }
            response = requests.request("POST", url, data=payload1, headers=headers, verify=False)
            print(response.text)
            rs = json.loads(response.text)                  
            msg_id = rs["messages"][0]["id"]   


            message1 = user_message()
            message1.wa_id = to
            message1.message = caption
            message1.name = name
            message1.m_type = type1
            message1.m_from = 'website'
            message1.timestamp1 = datetime.datetime.now()
            message1.m_status = 'unread'
            message1.m_fileName = filename
            message1.m_url = link
            message1.unique_msg_id = msg_id
            message1.save()
            return JsonResponse({"message": "success"})

        elif uploaded_file.content_type == 'image/png' or uploaded_file.content_type == 'image/jpg' or uploaded_file.content_type == 'image/jpeg':

            bi_data = request.FILES['browseFile'].read()
            url = url_main + "/v1/users/login"
            payload = "{\n\t\"new_password\": \""+pass_for_api+"\"\n}"
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Basic <base64(username:password)>',
                'Authorization': 'Basic ' + base_64 +"'"
            }
            response = requests.request("POST", url, headers=headers, data=payload, verify=False)
            rs = response.text
            json_data = json.loads(rs)
            authkey = json_data["users"][0]["token"]

            url = url_main + "/v1/media"
            payload = bi_data
            headers = {
                'Content-Type': 'image/jpeg',
                'Authorization': "Bearer " + authkey,
                'cache-control': "no-cache",
                'Postman-Token': "1083c9be-a60e-4a0d-94a4-448ef126085e",
            }
            response = requests.request("POST", url, data=payload, headers=headers, verify=False)
            rt = response.text
            json_data = json.loads(rt)
            img_id = json_data["media"][0]["id"]
            url = url_main + "/v1/messages/"

            payload1 = "{\n\t\"to\": \"" + to + "\", \n\t\"type\": \"image\", \n\t\"recipient_type\": \"individual\", \n\t\"image\": {\n\t\t\"id\": \"" + img_id + "\",\n\t\t\t\"caption\": \"" + caption + "\"\n\t\t}\n}\n"
            headers = {
                'Content-Type': "application/json",
                'Authorization': "Bearer " + authkey,
                'cache-control': "no-cache",
                'Postman-Token': "1083c9be-a60e-4a0d-94a4-448ef126085e"
            }
            response = requests.request("POST", url, data=payload1, headers=headers, verify=False)
            print(response.text)
            rs = json.loads(response.text)                  
            msg_id = rs["messages"][0]["id"]  
            encoded_data = base64.b64encode(bi_data)
            ts = calendar.timegm(time.gmtime())
            # rt = response.text
            # json_data = json.loads(rt)
            file1 = request.FILES['browseFile'].name
            file1 = str(ts) + "_" + file1
            fh = open(os.path.join(settings.MEDIA_ROOT + "/image/", file1), "wb")
            fh.write(base64.decodebytes(encoded_data))
            fh.close()
            message1 = user_message()
            message1.wa_id = to
            message1.message = caption
            message1.name = name
            message1.m_type = 'image'
            message1.m_from = 'website'
            message1.timestamp1 = datetime.datetime.now()
            message1.m_status = 'unread'
            message1.m_fileName = file1
            message1.m_url = "media/image/"
            message1.unique_msg_id = msg_id
            message1.save()
            return JsonResponse({"message": "success"})

        elif uploaded_file.content_type == 'video/mp4' or uploaded_file.content_type == 'video/avi':
            bi_data = request.FILES['browseFile'].read()
            url = url_main + "/v1/users/login"
            payload = "{\n\t\"new_password\": \""+pass_for_api+"\"\n}"
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Basic <base64(username:password)>',
                'Authorization': 'Basic ' + base_64 +"'"
            }
            response = requests.request("POST", url, headers=headers, data=payload, verify=False)
            rs = response.text
            json_data = json.loads(rs)
            authkey = json_data["users"][0]["token"]
            print(uploaded_file.content_type)
            url = url_main + "/v1/media"
            payload = bi_data
            headers = {
                'Content-Type': uploaded_file.content_type,
                'Authorization': "Bearer " + authkey,
                'cache-control': "no-cache"

            }
            response = requests.request("POST", url, data=payload, headers=headers, verify=False)
            rt = response.text
            json_data = json.loads(rt)
            img_id = json_data["media"][0]["id"]
            url = url_main + "/v1/messages/"

            payload1 = "{\n\t\"to\": \"" + to + "\", \n\t\"type\": \"video\", \n\t\"recipient_type\": \"individual\", \n\t\"video\": {\n\t\t\"id\": \"" + img_id + "\",\n\t\t\t\"caption\": \"" + caption + "\"\n\t\t}\n}\n"
            headers = {
                'Content-Type': "application/json",
                'Authorization': "Bearer " + authkey,
                'cache-control': "no-cache"

            }
            response = requests.request("POST", url, data=payload1, headers=headers, verify=False)
            print(response.text)
            rs = json.loads(response.text)                  
            msg_id = rs["messages"][0]["id"]   
            encoded_data = base64.b64encode(bi_data)
            ts = calendar.timegm(time.gmtime())
            rt = response.text
            json_data = json.loads(rt)
            file1 = request.FILES['browseFile'].name
            file1 = str(ts) + "_" + file1
            fh = open(os.path.join(settings.MEDIA_ROOT + '/video', file1), "wb")
            fh.write(base64.decodebytes(encoded_data))
            fh.close()
            message1 = user_message()
            message1.wa_id = to
            message1.message = caption
            message1.name = name
            message1.m_type = 'video'
            message1.m_from = 'website'
            message1.timestamp1 = datetime.datetime.now()
            message1.m_status = 'unread'
            message1.m_fileName = file1
            message1.m_url = "media/video/"
            message1.unique_msg_id = msg_id
            message1.save()
            return JsonResponse({"message": "success"})

        elif uploaded_file.content_type == 'application/pdf' or uploaded_file.content_type == 'text/plain' or uploaded_file.content_type == 'application/octet-stream':
            bi_data = request.FILES['browseFile'].read()
            url = url_main + "/v1/users/login"
            payload = "{\n\t\"new_password\": \""+pass_for_api+"\"\n}"
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Basic <base64(username:password)>',
                'Authorization': 'Basic ' + base_64 +"'"
            }
            response = requests.request("POST", url, headers=headers, data=payload, verify=False)
            rs = response.text
            json_data = json.loads(rs)
            authkey = json_data["users"][0]["token"]

            url = url_main + "/v1/media"
            payload = bi_data
            headers = {
                'Content-Type': uploaded_file.content_type,
                'Authorization': "Bearer " + authkey,
                'cache-control': "no-cache"

            }
            response = requests.request("POST", url, data=payload, headers=headers, verify=False)
            rt = response.text
            json_data = json.loads(rt)
            img_id = json_data["media"][0]["id"]
            url = url_main + "/v1/messages/"

            payload1 = "{\n\t\"to\": \"" + to + "\", \n\t\"type\": \"document\", \n\t\"recipient_type\": \"individual\", \n\t\"document\": {\n\t\t\"id\": \"" + img_id + "\",\n\t\t\t\"caption\": \"" + caption + "\"\n\t\t}\n}\n"
            headers = {
                'Content-Type': "application/json",
                'Authorization': "Bearer " + authkey,
                'cache-control': "no-cache"
                
            }
            response = requests.request("POST", url, data=payload1, headers=headers, verify=False)
            print(response.text)
            rs = json.loads(response.text)                  
            msg_id = rs["messages"][0]["id"]   
            encoded_data = base64.b64encode(bi_data)
            ts = calendar.timegm(time.gmtime())
            rt = response.text
            json_data = json.loads(rt)
            file1 = request.FILES['browseFile'].name
            file1 = str(ts) + "_" + file1
            fh = open(os.path.join(settings.MEDIA_ROOT + '/documents', file1), "wb")
            fh.write(base64.decodebytes(encoded_data))
            fh.close()
            message1 = user_message()
            message1.wa_id = to
            message1.message = caption
            message1.name = name
            message1.m_type = 'document'
            message1.m_from = 'website'
            message1.timestamp1 = datetime.datetime.now()
            message1.m_status = 'unread'
            message1.m_fileName = file1
            message1.m_url = "media/documents/"
            message1.unique_msg_id = msg_id
            message1.save()
            return JsonResponse({"message": "success"})

        else:
            return JsonResponse({"message": "fail"})

def check_message(request):

    wa_number = request.GET.get('wa_number', None)
    # return render(request,'step2.html')
    with connection.cursor() as cursor:
        sql_query = cursor.execute('SELECT sent_message from mywork_user_details where phone=%s;',[wa_number])
        sql_query_all = cursor.fetchall()
    for sql_query in sql_query_all:
        print(sql_query)

    try:
        status = sql_query[0]
        if status == '0':
            return JsonResponse({"status": status})
        else:
            return JsonResponse({"status": status})
    except:
        return JsonResponse({"status": '2'})

    status = str(sql_query[0])
    print(status)

    return JsonResponse({"status": status})


def update_authkey():
    url=url_main + "/v1/users/login"
    payload = "{\n\t\"new_password\": \""+pass_for_api+"\"\n}"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic ' + base_64 +"'"
            }
    response = requests.request("POST", url, headers=headers, data = payload,verify=False)
    rs=response.text
    json_data=json.loads(rs)
    return json_data["users"][0]["token"]


def check_contact(phone):
    authkey = update_authkey()
    url = url_main + "/v1/contacts"
    payload = '{"blocking": "wait","contacts": ["+91'+str(phone)+'"]}'
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer " + authkey
    }

    try:
        response = requests.request("POST", url.rstrip(), data=payload, headers=headers, verify=False)
        rs = response.text
        print(rs)
    except Exception as e:
        print(e)
    return ""

def send_template(request):
    to = request.GET.get('to', None)
    param1 = request.GET.get('param1', None)
    param2 = request.GET.get('param2', None)
    param3 = request.GET.get('param3', None)
    authkey = update_authkey()

    url = url_main + "/v1/messages/"
    # Payload of tag_callback
    payload = '{"to": "91'+ str(to) +'", "type": "template", "template": {"namespace": "8533d4ae_209a_48c4_847c_8b7e0bb86430", "name": "tb_paylink_three_param", "language": {"policy": "deterministic", "code": "en_US"}, "components": [ {"type": "body", "parameters": [{"type": "text", "text": "*'+param1+'*"}, {"type": "text", "text": "*'+param2+'*"}, {"type": "text", "text": "*'+param3+'*"}]}]}} '
    payload = '{"to": "91' + str(to) + '", "type": "template", "template": {"namespace": "10aac1cc_58ce_4275_8374_9b0ffd4b9de1", "name": "ktpl_reply", "language": {"policy": "deterministic", "code": "en"}, "components": [{"type": "header", "parameters": [{"type": "image", "image": {"link": "https://www.khairnar.tech/img/ktpllogo.png"}}]}, {"type": "body", "parameters": [{"type": "text", "text": "'+param1+'"}, {"type": "text", "text": "'+param2+'"}, {"type": "text", "text": "'+param3+'"}]}, {"type": "button", "sub_type": "quick_reply", "index": "2", "parameters": [{"type": "payload", "payload": "Payoad Text sended"}]}]}} '
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer " + authkey
    }
    try:

        # print(len(to),param1,param2,param3)
        if(to.isnumeric()==True and len(to)==10 ):
            # print('correct phone')
            if( param1 != "" and param2 != "" and param3 != ""):
                check_contact(to)
                response = requests.request("POST", url.rstrip(), data=payload.encode(), headers=headers, verify=False)
                rs = response.text
                # print('valid params')
            else:
                return JsonResponse({'status': 'Enter Valid Parameters'})

        else:
            return JsonResponse({'status': 'Enter valid 10 Digit number'})
    except Exception as e:
        print(e)
    return JsonResponse({'status': 'success'})


def check_timediff(request):
    phone = request.GET.get('phone', None)
    print(phone)
    try:
        with connection.cursor() as cursor:
            sql_query = cursor.execute('select timestamp1 from mywork_user_message where wa_id=%s ORDER BY timestamp1 DESC', [phone])
            sql_query_all = cursor.fetchall()

        for sql_query in sql_query_all:
            time = sql_query[0]
            print(time)
            break

        now = datetime.datetime.now()
        timediff = now - time
        # print(now, timediff)

        with connection.cursor() as cursor:
            message_query = cursor.execute('select message from mywork_user_message where wa_id=%s ORDER BY timestamp1 DESC', [phone])
            message_query_all = cursor.fetchall()

        for message_query in message_query_all:
            message = message_query[0]
            print(message)
            break
        message = message
    
        if timediff.total_seconds() > 86400.0000:
            # print("more")
            return JsonResponse({'diff':'more','message':''})
        else :
            return JsonResponse({'diff':'less','message':message})

    except Exception as e:
        print(e)
        return JsonResponse({'diff':'Error','message':""})


def error400(request):
    return render(request, 'error400.html')


def error500(request):
    #data = {}
    return render(request, 'error500.html')

@csrf_exempt
def webhook(request):    

    def download_media(id):
        authkey = update_authkey()
        url =  url_main + "/v1/media/" + id

        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer "+ authkey,
            'cache-control': "no-cache",
            'Postman-Token': "c7225772-08c7-43f8-b905-1b18da80d814"
            }
        response = requests.request("GET", url, headers=headers, verify = False)
        return response


    # def send_msg(frm, body):
    #     print("In def send_msg")
    #     authkey = update_authkey()
    #     url2 = url_main + "/v1/messages"
    #     options = {'Yes': '{"to": "'+str(frm)+'","type": "text","recipient_type": "individual","text": {"body": "Kya aap soch rahe hai, CLASS 11th KI PADHAI KAISE KARU, toh don’t worry!\\nJoin Free Live Batch on Vidyakul App -\\n\\n🚀Fast Track Concept Revision \\n✅Chaptr-wise Important Questions \\n📋Notes & Sample Paper - PDF \\n💡Mind Mapping for Exam \\n\\n🆓Sab Free Mein!😊\\n\\n📲Download Now ⬇️\\nhttps://vidyakul.onelink.me/qQal/whatsapp"},"preview_url": true}',
    #             'No': '{"to": "'+str(frm)+'","type": "text","recipient_type": "individual","text": {"body": "Kya aap soch rahe hai, CLASS 11th KI PADHAI KAISE KARU, toh don’t worry!\\nJoin Free Live Batch on Vidyakul App -\\n\\n🚀Fast Track Concept Revision \\n✅Chaptr-wise Important Questions \\n📋Notes & Sample Paper - PDF \\n💡Mind Mapping for Exam \\n\\n🆓Sab Free Mein!😊\\n\\n📲Download Now ⬇️\\nhttps://vidyakul.onelink.me/qQal/whatsapp"},"preview_url": true}',
    #             'Know More': '{"to": "'+str(frm)+'","type": "text","recipient_type": "individual","text": {"body": "Kya aap soch rahe hai, CLASS 11th KI PADHAI KAISE KARU, toh don’t worry!\\nJoin Free Live Batch on Vidyakul App -\\n\\n🚀Fast Track Concept Revision \\n✅Chaptr-wise Important Questions \\n📋Notes & Sample Paper - PDF \\n💡Mind Mapping for Exam \\n\\n🆓Sab Free Mein!😊\\n\\n📲Download Now ⬇️\\nhttps://vidyakul.onelink.me/qQal/whatsapp"},"preview_url": true}',
    #             }

    #     headers = {
    #         'Content-Type': "application/json",
    #         'Authorization': "Bearer " + authkey
    #     }
    #     b = body
    #     payload = options[b]
    #     paylod = payload.encode()

    #     try:
    #         response = requests.request("POST", url2.rstrip(), data=payload, headers=headers, verify=False)
    #         rs = response.text
    #     except Exception as e:
    #         print(e)
    print(request.method)
    print("Auth Printed Below")
    print(request.GET.get('auth',None))
    now = datetime.datetime.now()
    cnt=0
    response = json.loads(request.body)    

    print(response)
    print(response["statuses"][0]["status"])

    try:
        if "id" in response["statuses"][0]:            
            
            unique_msg_id = response["statuses"][0]["id"]
            status = response["statuses"][0]["status"]        
            
            with connection.cursor() as cursor:
                sql_query = cursor.execute('update mywork_user_message set unique_msg_status=%s where unique_msg_id=%s',[status, unique_msg_id])

            
            print("staus updated Successfully")

        phn = str(response["messages"][0]["from"])
        msg_type = response["messages"][0]["type"]
        timestamp = int(response["messages"][0]["timestamp"])
        id=""
        name=""
        timestamp1=""
        caption = ""
        unique_msg_id = str(response["messages"][0]["id"])
        print(msg_type)
        ## Text message
        if (msg_type == "button"):
            text = response["messages"][0]["button"]["text"]
            id = response["contacts"][0]["wa_id"]
            name = str(response["contacts"][0]["profile"]["name"])
            timestamp1=str(response["messages"][0]["timestamp"])
            type = str(response["messages"][0]["type"])
            
            m_id = ""
            m_url = ""
            file1 = ""
            caption = ""
            # send_msg(id, text)
            print("In Button")
            print(id,name,text,type,id,now,m_id,m_url,file1)


        if msg_type == "text" and len(phn) == 12:
            text = str(response["messages"][0]["text"]["body"])
            id = str(response["contacts"][0]["wa_id"])
            name = str(response["contacts"][0]["profile"]["name"])
            timestamp1=str(response["messages"][0]["timestamp"])
            type = str(response["messages"][0]["type"])
            m_id = ""
            m_url = ""
            file1 = ""
            caption = ""
            print("In text")
            print(id,name,text,type,id,now,m_id,m_url,file1)
            ## check if password
            ## yes: map user to client and store json_data
            ## no: map user to client and send data to client


            data = {
                "contacts": [
                    {
                        "wa_id": phn
                    }
                ],
                "messages": [
                    {
                        "from": phn,
                        "id": "ABEGkZEwEhhHAhBsB2_v7vWs6QdV7rbPWend",
                        "text": {
                            "body": text
                        },
                        "timestamp": timestamp,
                        "type": msg_type
                    }
                ]
            }


        ## Image message
        if msg_type == "image" and len(phn) == 12:

            id = str(response["contacts"][0]["wa_id"])
            name = str(response["contacts"][0]["profile"]["name"])
            timestamp1=str(response["messages"][0]["timestamp"])
            type = str(response["messages"][0]["type"])
            text = ''
            print(id,name,text,type,id,now)
            m_id = str(response["messages"][0]["image"]["id"])

            resp = download_media(m_id)
            image = resp.content
            encoded_data = base64.b64encode(image)
            ts = int(time.time())   
            m_url = "media/image/"  
            ext = str(response["messages"][0]["image"]["mime_type"])
            ext = ext.split("/", 1)[1]
            
            # if "caption" in response["messages"][0]["image"]["caption"]:           
            #     caption = str(response["messages"][0]["image"]["caption"])
            #     print(response["messages"][0]["image"]["caption"])

            if "caption" in response["messages"][0]["image"]:           
                caption = str(response["messages"][0]["image"]["caption"])
                print(response["messages"][0]["image"]["caption"])

            # content_type = mimetypes.guess_type(image)
            # print(content_type)
            
            file1 = 'image_' + str(ts) + "." + ext
            fh = open(os.path.join(settings.MEDIA_ROOT + "/image", file1), "wb")
            fh.write(base64.decodebytes(encoded_data))
            fh.close()
            print("In Image")
            print(id,name,text,type,id,now,m_id,m_url,file1) 


            data = {
                "contacts": [
                    {
                        "wa_id": phn
                    }
                ],
                "messages": [
                    {
                        "from": phn,
                        "id": "ABEGkZEwEhhHAhD92n2mbaU899-mlM-ollR5",
                        "image": {
                            "id": "da08fe56-fa6b-4709-8fdf-348b13973b6f",
                            "mime_type": "image/jpeg",
                            'body': image,
                            "sha256": "ae2694009475c44796eff23df09ffd72d1ded8c26e2a4bf38aaf0c745c6f29d7"
                        },
                        "timestamp": timestamp,
                        "type": msg_type
                    }
                ]
            }
        
        if msg_type == "video" and len(phn) == 12:
            id = str(response["contacts"][0]["wa_id"])
            name = str(response["contacts"][0]["profile"]["name"])
            timestamp1=str(response["messages"][0]["timestamp"])
            type = str(response["messages"][0]["type"])
            text = ''
                       
            m_id = str(response["messages"][0]["video"]["id"])
            if "caption" in response["messages"][0]["video"]:
                caption = str(response["messages"][0]["video"]["caption"])

            resp = download_media(m_id)
            video = resp.content
            encoded_data = base64.b64encode(video)
            ts = int(time.time())   
            m_url = "media/video/"  
            ext = str(response["messages"][0]["video"]["mime_type"])
            ext = ext.split("/", 1)[1]
            file1 = 'video_' + str(ts) + "." + ext
            fh = open(os.path.join(settings.MEDIA_ROOT + "/video", file1), "wb")
            fh.write(base64.decodebytes(encoded_data))
            fh.close()
            print("In Video")
            print(id,name,text,type,id,now,m_id,m_url,file1)


        if (msg_type == "voice" or msg_type == "audio" and len(phn) == 12):
            print("in audio voice")
            id = str(response["contacts"][0]["wa_id"])
            name = str(response["contacts"][0]["profile"]["name"])
            timestamp1=str(response["messages"][0]["timestamp"])
            type = str(response["messages"][0]["type"])
            text = ''
                       
            m_id = ""
            
            ts = int(time.time())   
            m_url = "media/voice/"  
            if msg_type == "voice":
                m_id = str(response["messages"][0]["voice"]["id"])
                ext = response["messages"][0]["voice"]["mime_type"]
                # if response["messages"][0]["audio"]["caption"]:
                #     caption = str(response["messages"][0]["voice"]["caption"])
                print(m_id)
                
            if msg_type == "audio":
                m_id = str(response["messages"][0]["audio"]["id"])
                ext = response["messages"][0]["audio"]["mime_type"]
                # if response["messages"][0]["audio"]["caption"]:
                #     caption = str(response["messages"][0]["audio"]["caption"])
                print(m_id)
                
            resp = download_media(m_id)
            media = resp.content
            encoded_data = base64.b64encode(media)

            print(ext)
            print("done")
            ext = ext.split("/")[1]
            print(ext)
            # ext = ext[0:3]
            file1 = 'video_' + str(ts) + "." + ext
            fh = open(os.path.join(settings.MEDIA_ROOT + "/voice", file1), "wb")
            fh.write(base64.decodebytes(encoded_data))
            fh.close()
            print("In Voice")
            print(id,name,text,type,id,now,m_id,m_url,file1)

        

        

            

        if msg_type == "document" and len(phn) == 12:
            id = str(response["contacts"][0]["wa_id"])
            name = str(response["contacts"][0]["profile"]["name"])
            timestamp1=str(response["messages"][0]["timestamp"])
            type = str(response["messages"][0]["type"])
            text = ''
            print(id,name,text,type,id,now)
            m_id = str(response["messages"][0]["document"]["id"])

            resp = download_media(m_id)
            
            if "caption" in response["messages"][0]["document"]:
                caption = str(response["messages"][0]["document"]["caption"])
            doc = resp.content
            encoded_data = base64.b64encode(doc)
            ts = int(time.time())   
            m_url = "media/documents/"  
            ext = str(response["messages"][0]["document"]["mime_type"])
            ext = ext.split("/", 2)[1]
            file1 = 'doc_' + str(ts) + "." + ext
            fh = open(os.path.join(settings.MEDIA_ROOT + "/documents", file1), "wb")
            fh.write(base64.decodebytes(encoded_data))
            fh.close()
            print("In Document")
            print(id,name,text,type,id,now,m_id,m_url,file1)


        

        user1 = user_message()
        user1.wa_id = id
        user1.name = name
        user1.m_media = m_id
        user1.message = text
        user1.m_type = msg_type
        user1.m_from = id
        user1.timestamp1 = now
        user1.m_url = m_url
        user1.m_fileName = file1
        user1.caption = caption
        user1.m_status = 'unread'
        user1.unique_msg_id = unique_msg_id
        user1.unique_msg_status = 'read'
        user1.save()
        
        print("Record inserted successfully into  table")
        if text =="Hello There, I want to know more about the Whatsapp Business API":           
            User_Details.objects
            user2 = User_Details(phone = phn[2:])
            user2.sent_message = 1
            user2.save()
            print("Changed status for user")



    except Exception as e:
        print(e)
        print("Exception Printed")

    return render(request,'step1.html')


def error400(request, exception):
    data = {}
    return render(request, 'error400.html', data)


def error500(request, exception):
    data = {}
    return render(request, 'error500.html', data)

