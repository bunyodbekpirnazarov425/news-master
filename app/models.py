from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Kategoriya nomi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

class News(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Yangilik nomi")
    slug = models.SlugField(max_length=255, verbose_name="Sluglar")
    description = models.TextField(blank=True, null=True, verbose_name="Ma'lumoti")
    image = models.ImageField(upload_to="news/images/",blank=True, null=True, verbose_name="Rasmi")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shish vaqti")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Maqola kategoriyasi")
    is_active = models.BooleanField(default=True, verbose_name="Saytga chiqarish")
    is_popular = models.BooleanField(default=True, verbose_name="Mashxur chiqarish")
    is_trending = models.BooleanField(default=True, verbose_name="Sara yangiliklar")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"
