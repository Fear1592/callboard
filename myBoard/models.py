from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse

from gallery.models import Gallery


class Category(MPTTModel):
    """Категории  объявлений"""
    name = models.CharField("Имя", max_length=50, unique=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    class MPTTMeta:
        order_insertion_by = ['name']


class FilterAdvert(models.Model):
    """Фильтр"""
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Фильтр"
        verbose_name_plural = "Фильтры"


class DateAdvert(models.Model):
    """Срок объявления"""
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Срок"
        verbose_name_plural = "Сроки"
        ordering = ['id']


class Advert(models.Model):
    """Объявления"""
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category,
        verbose_name="Категория",
        on_delete=models.CASCADE)
    filters = models.ForeignKey(
        FilterAdvert,
        verbose_name="Фильтр",
        on_delete=models.CASCADE
    )
    date = models.ForeignKey(
        DateAdvert,
        verbose_name="Срок",
        on_delete=models.CASCADE
    )
    subject = models.CharField("Тема", max_length=200)
    description = models.TextField("Объявление", max_length=10000)
    images = models.ForeignKey(
        Gallery,
        verbose_name="Изображения",
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    file = models.FileField(
        "Файл",
        upload_to="myBoard file/%Y/%m/%d/",
        blank=True,
        null=True
    )
    price = models.DecimalField("Цена", max_digits=100, decimal_places=2)
    slug = models.SlugField("url", max_length=200, unique=True)
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    moderation = models.BooleanField("Модерация", default=False)

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse("advert-detail",
                       kwargs={"category": self.category.slug,
                               "slug": self.slug})

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
