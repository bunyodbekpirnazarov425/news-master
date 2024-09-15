from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Kategoriya nomi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

    def get_newses(self):
        return News.objects.filter(category=self, is_active=True).order_by('-update')

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
    update = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")

    def get_image(self):
        if self.image:
            return f'<img src="{self.image.url}" alt="">'
        else:
            return "https://answers-afd.microsoft.com/static/images/image-not-found.jpg"

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"
