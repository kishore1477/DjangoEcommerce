from django import views
from django.urls import path
from shop import views
urlpatterns = [
    path('',views.index, name ="shop"  ),
    path('ind_temS',views.temSindex, name ="temSindex"  ),
    path('about/',views.about, name ="AboutUs"  ),
    path('contact/',views.contact, name ="ContactUs"  ),
    path('tracker/',views.tracker , name ="tracker"  ),
    path('search/',views.search , name ="search"  ),
    path('productView/',views.prodView , name ="productView"  ),
    path('checkout/',views.checkout  , name ="checkout"  ),
]
