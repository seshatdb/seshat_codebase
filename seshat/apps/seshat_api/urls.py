from django.urls import path, include
from rest_framework import routers

#from rest_framework.urlpatterns import format_suffix_patterns

from . import views
# from .views import PolityDetail, PolityList  # VarList, VarDetail


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'politys', views.PolityViewSet)
router.register(r'sections', views.SectionViewSet)


#router.register(r'references', views.ReferenceViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += [
    path('refs/', views.reference_list),
    path('refs/<int:pk>/', views.reference_detail),
    path('albums/', views.album_list),
    path('albums/<int:pk>/', views.album_detail),
]
# urlpatterns = [
#     #path('<int:pk>/', VarDetail.as_view(), name='detailcreate'),
#     #path('', VarList, name='api_home'),
#     path('<int:pk>/', PolityDetail.as_view(), name='detailcreate'),
#     path('', PolityList.as_view(), name='api_home'),
# ]

# urlpatterns_with_suffix = [
#     path('refs/', views.reference_list),
#     path('refs/<int:pk>/', views.reference_detail),
# ]
# urlpatterns = format_suffix_patterns(urlpatterns_with_suffix)
