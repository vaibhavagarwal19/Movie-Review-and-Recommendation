# project/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include('reviews.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls')),  # for login/logout
    path('docs/', include_docs_urls(title='Movie Review API')),
]
