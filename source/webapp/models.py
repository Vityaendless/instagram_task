from django.db import models
from django.contrib.auth import get_user_model


class AbstractModel(models.Model):
    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    class Meta:
        abstract = True


class Publication(AbstractModel):
    content = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Content")
    author = models.ForeignKey(get_user_model(), related_name='publications', on_delete=models.CASCADE, verbose_name="Author")
    img = models.ImageField(upload_to='publications_images', verbose_name='Avatar')
    likes_count = models.IntegerField(default=0, verbose_name='Count of likes')
    comments_count = models.IntegerField(default=0, verbose_name='Count of comments')
