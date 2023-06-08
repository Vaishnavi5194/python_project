from django.urls import path
from.import views


urlpatterns = [
    path('', views.homepage, name='webpage'),
    path('index', views.userreg, name='index'),
    path('login', views.userlogin, name='login'),
    path('logout', views.userlogout, name='logout'),
    path('home', views.userhome, name='home'),
    path('adhome', views.dephome, name='adhome'),
    path('adlogin', views.deplogin, name='adlogin'),
    path('deplogout', views.deplogout, name='deplogout'),
    path('adreg', views.depregister, name='adreg'),
    path('comview', views.usercomplaintdisplay, name='comview'),
    path('complaint', views.complaintreg, name='complaint'),
    path('complaintview', views.complaintdisplay, name='complaintview'),
    path('about', views.about,name='about'),
    path('contact', views.contact, name='contact'),
    path('support', views.support,name='support'),
    path('terms', views.terms, name='terms'),
    path('test', views.test, name='test'),
    path('head', views.adminlogin, name='head'),
    path('adprofile', views.adminlogin1, name='adprofile'),
    path('signout', views.adminlogout, name='signout'),
    # path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('rest', views.admin_change_password, name='rest'),
    path('rest1', views.user_change_password, name='rest1'),
    path('rest2', views.department_change_password, name='rest2'),

]