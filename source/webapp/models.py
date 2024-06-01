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

    def increase_count(self, marker):
        match marker:
            case 'likes':
                self.likes_count += 1
            case 'comments':
                self.comments_count += 1
        self.save()


class Subscription(models.Model):
    user = models.ForeignKey(
        get_user_model(), related_name='user_subscribers',
        on_delete=models.CASCADE, verbose_name='User'
    )
    subscriber = models.ForeignKey(
        get_user_model(), related_name='subscriber_users',
        on_delete=models.CASCADE, verbose_name='Subscriber'
    )


class Like(models.Model):
    user = models.ForeignKey(
        get_user_model(), related_name='user_publications',
        on_delete=models.CASCADE, verbose_name='User'
    )
    publication = models.ForeignKey(
        Publication, related_name='publication_users',
        on_delete=models.CASCADE, verbose_name='Publication'
    )


# class Comment(AbstractModel):
#    publication = models.ForeignKey('webapp.Publication', related_name='comments', on_delete=models.CASCADE, verbose_name='Comment')
#    text = models.TextField(max_length=400, verbose_name='Comment')
#    #author = models.CharField(max_length=40, null=True, blank=True, default='Аноним', verbose_name='Автор')
#    author = models.ForeignKey(get_user_model(), default=1, related_name='comments', on_delete=models.CASCADE,
#                               verbose_name="Author")
