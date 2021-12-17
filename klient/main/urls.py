from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('delivery/', views.delivery, name='delivery'),
    path('lookorders/', views.lookorders, name='lookorders'),
    path('storage/', views.storage, name='storage'),
    path('order_delivery/', views.orderDelivery, name='order_delivery'),
    path('warehouse/', views.warehouse, name='warehouse'),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

