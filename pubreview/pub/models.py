from django.db import models

# Create your models here.


class Pub(models.Model):
    name = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=100, blank=False)
    postal_code = models.CharField(max_length=10)
    description = models.TextField(blank=True, null=True)
    website = models.URLField()
    slug = models.SlugField(null=True, blank=True)
    pub_image = models.ImageField(upload_to=None, blank=True, null=True)

    def __str__(self):
    	return self.name