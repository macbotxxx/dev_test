from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(
        verbose_name="Blog title",
        max_length=255,
        null=True,
        blank=False,
        help_text="Blog title of the blog"
    )

    body = models.TextField(
        verbose_name="Blog title",
        null=True,
        blank=False,
        help_text="Blog title of the blog"
    )

    created_date = models.DateTimeField(
        verbose_name="Created date",
        auto_now_add=True,
        null=True,
        help_text="this stroes the actual date and time for the blog"
    )

    modified_date = models.DateTimeField(
        verbose_name="Created date",
        auto_now=True,
        null=True,
        help_text="this stroes the updated date and time when the blog was updated last"
    )

    def __str__(self) :
        return str(self.title)