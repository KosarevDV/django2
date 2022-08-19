from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from mainapp import views as mainapp

urlpatterns = [
    path("admin/", admin.site.urls),
    path("admin_staff/", include("adminapp.urls", namespace="admin_staff")),
    path("", mainapp.index, name="main"),
    path("contact/", mainapp.contact, name="contact"),
    path("products/", include("mainapp.urls", namespace="products")),
    path("auth/", include("authapp.urls", namespace="auth")),
    path("basket/", include("basketapp.urls", namespace="basket")),
    path('', include('social_django.urls', namespace='social')),
    path('orders/', include("ordersapp.urls", namespace="orders"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
