from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
# Create your models here.
class Post(models.Model):

    title       = models.CharField(max_length=50)
    slug        = models.SlugField(max_length=200, unique=True, blank=True) # added on Jan 7th
    author      = models.ForeignKey(User, on_delete=models.CASCADE)
    category    = models.ForeignKey('blog.Category', verbose_name="Category", blank=True, on_delete=models.CASCADE)
    tags        = models.ManyToManyField("blog.Tag", verbose_name="Tag", blank=True)
    content     = models.TextField()
    create_on   = models.DateTimeField(auto_now_add=True)
    updated_on  = models.DateField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    # content = models.TextInput()
    class Meta:
        ordering = ['-updated_on']
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Post_detail", kwargs={"pk": self.pk})

class Category(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={"pk": self.pk})

class Tag(models.Model):

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Tag_detail", kwargs={"pk": self.pk})
