from django.urls import path

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

]
