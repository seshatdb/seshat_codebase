from django.urls import path, include

#from django.conf.urls import url

from . import views
from .models import Seshat_Task

urlpatterns = [
    path('', views.accounts, name='accounts'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('userprofile/', views.profile, name='user-profile'),
]

urlpatterns += [
    path('seshat_task/create/', views.Seshat_taskCreate.as_view(),
         name="seshat_task-create"),

    # path('seshat_tasks/', views.Seshat_taskListView.as_view(), name='seshat_tasks'),
    path('seshat_task/<int:pk>', views.Seshat_taskDetailView.as_view(),
         name='seshat_task-detail'),
    # path('seshat_task/<int:pk>/update/',
    #      views.Seshat_taskUpdate.as_view(), name="seshat_task-update"),
    # path('seshat_task/<int:pk>/delete/',
    #      views.Seshat_taskDelete.as_view(), name="seshat_task-delete"),
]
    

urlpatterns += [ path('profile/<int:pk>/update/', views.ProfileUpdate.as_view(), name="profile-update"),]
#urlpatterns += patterns('accounts.views',
                    #    url(r'^view_profile/$', 'view_profile', name ='view_profile'),
                    #    url(r'^view_profile/edit_profile/$', 'edit_profile', name ='edit_profile'))