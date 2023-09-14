from django.urls import path, re_path

from . import views

urlpatterns = [path('', views.seshatindex, name='seshat-index'),]
urlpatterns += [path('methods', views.seshatmethods, name='seshat-methods'),]
urlpatterns += [path('whoweare', views.seshatwhoweare, name='seshat-whoweare'),]
urlpatterns += [path('acknowledgements', views.seshatacknowledgements, name='seshat-acknowledgements'),]

urlpatterns += [path('polity_filter_options/', views.polity_filter_options_view, name='polity_filter_options'),]


urlpatterns += [
     path('core/references/', views.ReferenceListView.as_view(), name='references'),
     path('core/nlp-references/', views.NlpReferenceListView.as_view(), name='nlp-references'),
     path('core/references/create/', views.ReferenceCreate.as_view(),
         name="reference-create"),
     path('core/references/<int:pk>', views.ReferenceDetailView.as_view(),name='reference-detail'),
     path('core/references/<int:pk>/update/',views.ReferenceUpdate.as_view(), name="reference-update"),
    path('core/references/<int:pk>/delete/', views.ReferenceDelete.as_view(), name="reference-delete"),
        path('core/references/no_zotero_refs_list/', views.no_zotero_refs_list, name='no_zotero_refs_list'),
     path('core/references/<int:pk>/updatemodal/', views.reference_update_modal, name='reference_update_modal'),
     path('referencesdownload/', views.references_download,
         name="references_download"),

    path('core/polities/create/', views.PolityCreate.as_view(),
         name="polity-create"),
    path('core/polities/', views.PolityListView.as_view(), name='polities'),
    path('core/polity/<int:pk>', views.PolityDetailView.as_view(), name='polity-detail-main'),
     path('core/polities/<int:pk>/update/',
         views.PolityUpdate.as_view(), name="polity-update"),


    path('core/ngas/create/', views.NgaCreate.as_view(),
         name="nga-create"),
    path('core/ngas/', views.NgaListView.as_view(), name='ngas'),
    path('core/nga/<int:pk>', views.NgaDetailView.as_view(), name='nga-detail'),
     path('core/ngas/<int:pk>/update/',
         views.NgaUpdate.as_view(), name="nga-update"),

    path('core/capitals/create/', views.CapitalCreate.as_view(),
         name="capital-create"),
    path('core/capitals/', views.CapitalListView.as_view(), name='capitals'),
     path('core/capitals/<int:pk>/update/',
         views.CapitalUpdate.as_view(), name="capital-update"),
    path('core/capitals/<int:pk>/delete/',
         views.CapitalDelete.as_view(), name="capital-delete"),
     path('capitaldownload/', views.capital_download,
         name="capital-download"),



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
     path('synczotero100/', views.synczotero100, name='synczotero100'),
     path('updatecitations/', views.update_citations, name='updatecitations'),
]

urlpatterns += [
    path('core/citations/create/', views.CitationCreate.as_view(),
         name="citation-create"),
     path('core/citations/', views.CitationListView.as_view(), name='citations'),
    path('core/citations/<slug:id>', views.CitationDetailView.as_view(),
         name='citation-detail'),
    path('core/citations/<slug:pk>/update/',
         views.CitationUpdate.as_view(), name="citation-update"),
    path('core/citations/<int:pk>/delete/',
         views.CitationDelete.as_view(), name="citation-delete"),
    # Download
    #path('balancedownload/', views.balance_download,
     #    name="balance-download"),
]

urlpatterns += [
    path('core/seshatcomments/create/', views.SeshatCommentCreate.as_view(),
         name="seshatcomment-create"),
     path('core/seshatcomments/', views.SeshatCommentListView.as_view(), name='seshatcomments'),
    path('core/seshatcomments/<slug:id>', views.SeshatCommentDetailView.as_view(),
         name='seshatcomment-detail'),
    path('core/seshatcomments/<int:pk>/update/',
         views.SeshatCommentUpdate.as_view(), name="seshatcomment-update"),
    path('core/seshatcomments/<int:pk>/delete/',
         views.SeshatCommentDelete.as_view(), name="seshatcomment-delete"),
    # Download
    #path('balancedownload/', views.balance_download,
     #    name="balance-download"),
]

urlpatterns += [
    path('core/seshatcommentparts/create/', views.SeshatCommentPartCreate.as_view(),
         name="seshatcommentpart-create"),
    path('core/seshatcommentparts/create2/<int:com_id>/<int:subcom_order>/', views.SeshatCommentPartCreate2.as_view(),
         name="seshatcommentpart-create2"),
     path('core/seshatcommentparts/', views.SeshatCommentPartListView.as_view(), name='seshatcommentparts'),
    path('core/seshatcommentparts/<slug:id>', views.SeshatCommentPartDetailView.as_view(),
         name='seshatcommentpart-detail'),
    path('core/seshatcommentparts/<int:pk>/update/',
         views.SeshatCommentPartUpdate.as_view(), name="seshatcommentpart-update"),
    path('core/seshatcommentparts/<int:pk>/delete/',
         views.SeshatCommentPartDelete.as_view(), name="seshatcommentpart-delete"),
    # Download
    #path('balancedownload/', views.balance_download,
     #    name="balance-download"),
]

urlpatterns += [path('core/discussion_room/', views.discussion_room, name="discussion_room"),]
urlpatterns += [path('core/nlp_datapoints/', views.nlp_datapoints, name="nlp_datapoints"),]
urlpatterns += [path('core/nlp_datapoints_2/', views.nlp_datapoints_2, name="nlp_datapoints_2"),]

urlpatterns += [
     path('core/not_found_404', views.four_o_four,
         name="four-o-four"),
]