from django.urls import path
from . import views


# ViewSet을 사용하면 아래처럼 어떤 메소드에 어떤 행위를 할 건지 써줘야하나보다.
urlpatterns = [
    path("", views.CategoryViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "<int:pk>/",
        views.CategoryViewSet.as_view(
            {"get": "retrieve", "put": "partial_update", "delete": "destroy"}
        ),
    ),
]
