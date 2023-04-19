from django.db import models


class CategoryInformation(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False, verbose_name="Название категории")

    class Meta:
        verbose_name = "Категория информаций"
        verbose_name_plural = "Категории информаций"

    def __str__(self):
        return self.title


class SubcategoryInformation(models.Model):
    profile_picture = models.ImageField(upload_to="info_data/profile_picture", null=True, blank=False,
                                        verbose_name="Картинка")
    title = models.CharField(max_length=255, blank=False, null=False, verbose_name="Название подкатегории")
    description = models.TextField(null=True, blank=False, verbose_name="Описание")
    block = models.ForeignKey(CategoryInformation, on_delete=models.PROTECT, related_name='block',
                                    verbose_name="Название главной категории")

    class Meta:
        verbose_name = "Подкатегория информаций"
        verbose_name_plural = "Подкатегории информаций"

    def __str__(self):
        return self.title

