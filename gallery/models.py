from django.db import models


class Photo(models.Model):
    """Фото"""
    name = models.CharField(max_length=50, unique=True)
    image = models.ImageField("Фото", upload_to="gallery/%Y/%m/%d/")
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


class Gallery(models.Model):
    """Галерея"""
    name = models.CharField(max_length=50, unique=True)
    photos = models.ManyToManyField(Photo, verbose_name="Фотогорафии")
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галереи"
