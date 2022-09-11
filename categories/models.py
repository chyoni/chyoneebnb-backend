from tabnanny import verbose
from django.db import models
from common.models import CommonModel


class Category(CommonModel):

    """Room or Experience Category"""

    class CategoryKindChoices(models.TextChoices):
        ROOMS = ("rooms", "Rooms")
        EXPERIENCES = ("experiences", "Experiences")

    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=15, choices=CategoryKindChoices.choices)

    def __str__(self) -> str:
        # title()은 첫글자 대문자로 만들어주는 메소드
        return f"{self.kind.title()}: {self.name}"

    class Meta:
        verbose_name_plural = "categories"
