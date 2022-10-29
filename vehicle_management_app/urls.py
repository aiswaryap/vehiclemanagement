from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.fun,name='fun'),
    path('add/',views.add_vehicle,name='add_vehicle'),
    path('detail/<int:vehicle_id>',views.detail,name='detail'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete, name='delete'),
    path('about/',views.about, name='about'),
    path('source/',views.source, name='source')
]