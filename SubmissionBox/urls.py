from django.conf.urls import url, include
from django.contrib.auth.models import User
from django.contrib import admin
from django.conf.urls.static import static
from rest_framework import routers, serializers, viewsets
from . import settings
from upload import views

admin.site.site_header = settings.ADMIN_SITE_HEADER

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'uploads', views.UploadViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^submit/', views.submit),
    url(r'^review/', views.review),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
