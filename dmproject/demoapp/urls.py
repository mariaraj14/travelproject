from.import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),
    #path('about/',views.about,name='about'),
    # path('add/',views.add,name='addition')
    # path('detail/',views.detail,name='detail')
]