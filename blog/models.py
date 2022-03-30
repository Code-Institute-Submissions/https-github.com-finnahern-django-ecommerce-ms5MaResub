from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    """
    Data model for blog posts
    """
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date="publish")
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="blog_posts")
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-publish",)

    def save(self, *args, **kwargs):
        """
        Generate an slug and publish date if they haven't been set already
        """
        if not self.slug:
            self.slug = self.title.lower().replace(" ", "-")
        if not self.publish:
            self.publish = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_post",
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.publish.hour,
                             self.publish.minute,
                             self.slug])

    def get_edit_url(self):
        return reverse("edit_post",
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.publish.hour,
                             self.publish.minute,
                             self.slug])
