"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from blogapp.api_views import CategoryViewSet, PostViewSet, TagViewSet

# router = routers.DefaultRouter()
# router.register(r'categories', CategoryViewSet)
#
# router = routers.DefaultRouter()
# router.register(r'posts', PostViewSet)

# router = routers.DefaultRouter()
# router.register(r'categories', CategoryViewSet)
# router.register(r'posts', PostViewSet)
# router.register(r'tags', TagViewSet)

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'posts', PostViewSet, basename='post')
router.register(r'tags', TagViewSet, basename='tag')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogapp.urls', namespace='blog')),
    path('users/', include('usersapp.urls', namespace='users')),
    #path('users/', include('usersapp.urls', namespace='users'))
    path('api-auth/', include('rest_framework.urls')),
    # path('api/v0/categories/', include(router.urls)),
    # path('api/v0/posts/', include(router.urls)),
    path('api/v0/', include(router.urls)),

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        #path('', views.home, name='home'),  # Обработчик для главной страницы
    ] + urlpatterns


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

