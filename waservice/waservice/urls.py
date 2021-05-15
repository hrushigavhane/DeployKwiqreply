from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path
from mywork import views


urlpatterns = [
     path('', views.home, name='home'),
     path('login', views.login, name='login'),
     path('login_success', views.login_success, name='login_success'),
     path('login_verify', views.login_verify, name='login_verify'),
     path('register', views.register, name='register'),
     path('resend_link', views.resend_link, name='resend_link'),
     path('forgot_password', views.forgot_password, name='forgot_password'),
     path('password_verify', views.password_verify, name='password_verify'),
     url(r'^recover_password/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.recover_password, name='recover_password'),
     url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
     url('logout', views.logout, name='logout'),
     url('dashboard', views.dashboard, name='dashboard'),
     url('sandbox', views.sandbox, name='sandbox'),
     url('senders', views.senders, name='senders'),
     url('senderno', views.senderno, name='senderno'),
     url('logs', views.logs, name='logs'),
     url('insight1', views.insight1, name='insight1'),
     url('insight2', views.insight2, name='insight2'),
     url('usage', views.usage, name='usage'),
     url('viewuse', views.viewuse, name='viewuse'),
     url('general_settings', views.general_settings, name='general_settings'),
     # url('channels_settings', views.channels_settings, name='channels_settings'),
     url('businessprofile', views.businessprofile, name='businessprofile'),
     url('configureno', views.configureno, name='configureno'),
     url('profile', views.profile, name='profile'),
     url('support', views.support, name='support'),
     url('submit_ticket', views.submit_ticket, name='submit_ticket'),
     url('ticket_history', views.ticket_history, name='ticket_history'),
     url('chat_window', views.chat_window, name='chat_window'),
     url('sales', views.sales, name='sales'),
     url('step1', views.step1, name='step1'),
     url('step2', views.step2, name='step2'),
     url('step3', views.step3, name='step3'),
     url('step4', views.step4, name='step4'),
     url('step5', views.step5, name='step5'),
     url('converse', views.converse, name='converse'),
     url('chat_statistics', views.chat_statistics, name='chat_statistics'),
     url('audience', views.audience, name='audience'),
     url('announce', views.announce, name='announce'),
     url('create_new_ant', views.create_new_ant, name='create_new_ant'),
     url('session_manage', views.session_manage, name='session_manage'),
     url('post_session', views.post_session, name='post_session'),
     url('notification_api', views.notification_api, name='notification_api'),
     url('admin_section', views.admin_section, name='admin_section'),
     url('admin_panel', views.admin_panel, name='admin_panel'),
     url('admin_registered_user', views.admin_registered_user, name='admin_registered_user'),
     url('admin_ticket_submission', views.admin_ticket_submission, name='admin_ticket_submission'),
     url('admin_sale_submission', views.admin_sale_submission, name='admin_sale_submission'),
     url('admin_business_p', views.admin_business_p, name='admin_business_p'),
     url(r'^ajax/send_message/$', views.send_message, name='send_message'),
     url(r'^ajax/get_chat/$', views.get_chat, name='get_chat'),
     url(r'^ajax/get_unread/$', views.get_unread, name='get_unread'),
     url(r'^ajax/update_status/$', views.update_status, name='update_status'),
     url(r'^ajax/get_count/$', views.get_count, name='get_count'),
     url(r'^ajax/send_file/$', views.send_file, name='send_file'),
     url(r'^ajax/search/$', views.search, name='search'),
     url(r'^ajax/check_message/$', views.check_message, name='check_message'),
     url(r'^ajax/send_template/$', views.send_template, name='send_template'),
     url(r'^ajax/check_timediff/$', views.check_timediff, name='check_timediff'),
     url('error500', views.error500, name='error500'),
     url('error400', views.error400, name='error400'),
     url('webhook', views.webhook, name='webhook')
     
]
'''
handler400 = 'mywork.views.error400'
handler403 = 'mywork.views.error400'
handler404 = 'mywork.views.error400'
handler500 = 'mywork.views.error500'
'''
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)