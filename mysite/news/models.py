from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model


User = get_user_model()


class Category(models.Model):
    title = models.CharField("name of category", max_length=50)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField("tag", max_length=50)

    class Meta:
        verbose_name = "tag"
        verbose_name_plural = "tags"

    def __str__(self):
        return self.title


class Articles(models.Model):
    user = models.ForeignKey(User,
                             verbose_name="author",
                             on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name="category",
                                 on_delete=models.SET_NULL,
                                 null=True)
    title = models.CharField("Title",
                             max_length=100)
    description = models.CharField("Description",
                                   max_length=100)
    post = models.TextField()
    keywords = models.CharField("Keywords",
                                max_length=50)
    tags = models.ManyToManyField(Tag,
                                  verbose_name="tag")
    list_date = models.DateTimeField(default=datetime.now,
                                     blank=True)
    image = models.ImageField(upload_to='media/img',
                              null=True,
                              blank=True)
    is_published = models.BooleanField(default=True)


    class Meta:
        verbose_name = "article"
        verbose_name_plural = "articles"

    def __str__(self):
        return self.title


class Comments(models.Model):
    user = models.ForeignKey(User,
                             verbose_name="User",
                             on_delete=models.CASCADE)
    new = models.ForeignKey(Articles,
                            verbose_name="article",
                            on_delete=models.CASCADE)
    text = models.TextField("comment")
    created = models.DateTimeField("date created", auto_now_add="True", null="True")
    moderation = models.BooleanField(default=False)


    class Meta:
        verbose_name = "comment"
        verbose_name_plural = "comments"

    def __str__(self):
        return "{}".format(self.user)