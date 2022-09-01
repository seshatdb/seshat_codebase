from django.urls import path, re_path

from . import views

urlpatterns = [path('', views.seshatindex, name='seshat-index'),]

urlpatterns += [
     path('core/references/', views.ReferenceListView.as_view(), name='references'),
    path('core/polities/', views.PolityListView.as_view(), name='polities'),
    path('core/polity/<int:pk>', views.PolityDetailView.as_view(), name='polity-detail'),
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
         name='variablehierarchysetting'),
     path('synczotero/', views.synczotero, name='synczotero'),
     path('updatecitations/', views.update_citations, name='updatecitations'),
]

urlpatterns += [
    path('core/citations/create/', views.CitationCreate.as_view(),
         name="citation-create"),
     path('core/citations/', views.CitationListView.as_view(), name='citations'),
    path('core/citations/<slug:id>', views.CitationDetailView.as_view(),
         name='citation-detail'),
    path('core/citations/<int:pk>/update/',
         views.CitationUpdate.as_view(), name="citation-update"),
    path('core/citations/<int:pk>/delete/',
         views.CitationDelete.as_view(), name="citation-delete"),
    # Download
    #path('balancedownload/', views.balance_download,
     #    name="balance-download"),
]

urlpatterns += [
     path('core/not_found_404', views.four_o_four,
         name="four-o-four"),
]