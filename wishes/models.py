from django.db import models

# Create your models here.

class Wishlist(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Список желаний"
        verbose_name_plural = "Списки желаний"


class Gift(models.Model):
    wishlist = models.ForeignKey(
        Wishlist,
        on_delete=models.CASCADE,
        related_name="gifts",
        verbose_name="Список желаний",
    )
    name = models.CharField(max_length=200, verbose_name="Подарок")
    price = models.PositiveIntegerField(blank=True, null=True, verbose_name="Цена, ₸")
    link = models.URLField(blank=True, verbose_name="Ссылка")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подарок"
        verbose_name_plural = "Подарки"