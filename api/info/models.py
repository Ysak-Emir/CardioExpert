from django.db import models


class CategoryInformation(models.Model):
    title_rus = models.CharField(max_length=255, blank=False, null=False, verbose_name="Название категории (rus)")
    title_kz = models.CharField(max_length=255, blank=False, null=False, verbose_name="Название категории (kz)")

    class Meta:
        verbose_name = "Категория информаций"
        verbose_name_plural = "Категории информаций"

    def __str__(self):
        return f'{self.title_rus}'


class SubcategoryInformation(models.Model):
    profile_picture = models.ImageField(upload_to="info_data/profile_picture", null=True, blank=False,
                                        verbose_name="Картинка")
    title_rus = models.CharField(max_length=255, blank=False, null=False, verbose_name="Название подкатегории (rus)")
    title_kz = models.CharField(max_length=255, blank=False, null=False, verbose_name="Название подкатегории (kz)")
    description_rus = models.TextField(null=True, blank=False, verbose_name="Описание (rus)")
    description_kz = models.TextField(null=True, blank=False, verbose_name="Описание (kz)")
    block = models.ForeignKey(CategoryInformation, on_delete=models.PROTECT, related_name='block',
                                    verbose_name="Название главной категории")

    class Meta:
        verbose_name = "Подкатегория информаций"
        verbose_name_plural = "Подкатегории информаций"

    def __str__(self):
        return f'{self.title_rus}'

