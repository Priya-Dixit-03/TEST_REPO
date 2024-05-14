from django.urls import path
from . views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home),
    path('ragistration/',create_user),
    path('table/',data),
    path('delete/<int:pk>/',delete_user, name="delete"),
    path("update/<int:uid>/", update, name="update"),
    path("update_user/", update_user),
    path('login_us/',login),
    path('login/',login_user),
    path('product/',product),
    path('add_product/',add_product)
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
