from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/rooms/", include("rooms.urls")),
    path("api/v1/categories/", include("categories.urls")),
    path("api/v1/experiences/", include("experiences.urls")),
    path("api/v1/medias/", include("medias.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# static()은 실제 파일의 위치는 settings.MEDIA_ROOT에서 찾고 그 사진의 URL을 MEDIA_URL로 설정해서 사진을 웹에서 보여준다는 의미 
