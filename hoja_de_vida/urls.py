from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('api/cv/', views.cv_api, name='cv_api'),
    # Catch-all for SPA handling (must be last)
    re_path(r'^.*$', views.IndexView.as_view(), name='index_catchall'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
