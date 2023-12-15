from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from movies.views import MovieViewSet,ActionViewSet,RemonceViewSet
from django.conf.urls.static import static
from django.conf import settings 


# Création des routes pour afficher l'api
router = routers.SimpleRouter()
router.register('movies',MovieViewSet)
router.register('action',ActionViewSet)
router.register('Remonce',RemonceViewSet)

# Inclure les routes dans l'api
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
