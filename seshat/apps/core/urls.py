from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.seshatindex, name='seshat-index')
]

urlpatterns += [
    path('core/polities/', views.PolityListView.as_view(), name='polities'),
    path('core/polity/<int:pk>', views.PolityDetailView.as_view(),
         name='polity-detail'),
    path('signup/', views.signup, name='signup'),
    path('signup_followup/', views.signupfollowup, name='signup-followup'),
    # re_path(r'^account_activation_sent/$', views.account_activation_sent,
    #         name='account_activation_sent'),
    # re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #         views.activate, name='activate'),
    path('account_activation_sent/', views.account_activation_sent,
         name='account_activation_sent'),
    path('activate/<slug:uidb64>/<slug:token>/',
         views.activate, name='activate'),
    path('variablehierarchy/', views.variablehierarchysetting,
         name='variablehierarchy'),

]
