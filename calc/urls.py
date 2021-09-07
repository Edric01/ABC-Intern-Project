from os import name
from django.urls import path
from . import views
urlpatterns = [
    path('',views.login,name='login'),
    path('logout',views.logout,name='home'),
    path('home',views.home,name='home'),
    path('register',views.register,name='register'),
    path('Services',views.services,name='services'),
    path('form',views.feedback,name='feedback'),
    path('kyc',views.kyc,name='kyc'),
    path('kyccreate',views.kyccreate,name='createKYC'),
    path('searchkyc',views.searchkyc,name='searchKYC'),
    path('editkyc',views.editkyc,name='editKYC'),
    path('reset',views.reset,name='reset-password'),
    path('research',views.research,name='Re-enter'),
    path('viewkyc',views.viewkyc,name='View-KYC'),
    path('verifysearch',views.verifysearch,name='Verify-KYC'),
    path('accounts',views.accounts,name='Accounts'),
    path('editsearch',views.editsearch,name='Search'),
    path('accsearch',views.accsearch,name='Search'),
    path('acccreate',views.acccreate,name='A/c-Creation'),
    path('accresearch',views.accresrch,name='A/c Search'),
    path('rateofinterest',views.rate,name='rateofinterest'),
]
