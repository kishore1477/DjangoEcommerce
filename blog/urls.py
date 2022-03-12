# from django import views
from django.urls import path
from  blog import views
urlpatterns = [
    path('',views.index, name ="blog"  ),
    path('contact/',views.contactBlog , name ="contact"  ),
    path('about/',views.aboutBlog , name ="about"  ),
    # path('',views.shop, name ="shop"  ),
    path('ind_temB',views.temBindex, name ="ind_temB"  ),
]
