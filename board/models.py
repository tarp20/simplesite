from django.db import models


class Bb(models.Model):
    title = models.CharField(max_length=200, verbose_name="Good")
    content = models.TextField(
        null=True, blank=True, verbose_name="Description")
    price = models.FloatField(null=True, blank=True, verbose_name="Price")
    published = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name="published")

    class Meta:
        verbose_name_plural = "announcements"
        verbose_name = "announcement"
        ordering = ['-published']
