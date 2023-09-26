from django.urls import path, include
from . import views
urlpatterns = [
   path('',views.home,name='home'),
   # path('details',views.details,name='details')
   path('delete/<int:delete_task>/',views.delete,name='delete'),
   path('update/<int:update_data>/',views.update,name='update'),
   path('cbvhome/',views.tasklistview.as_view(),name='cbvhome'),
   path('cbvdetail/<int:pk>/',views.detailview.as_view(),name='cbvdetail'),
   path('cbvedit/<int:pk>/',views.updateview.as_view(),name='cbvedit'),
   path('cbvdelete/<int:pk>/',views.deleteview.as_view(),name='cbvdelete'),

]
