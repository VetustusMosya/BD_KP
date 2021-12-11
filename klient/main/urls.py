from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    # path('ddd/', views.auto, name='auto'),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)