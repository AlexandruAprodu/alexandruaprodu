from django.db import models
from django.utils import timezone


class Prime(models.Model):
    title = models.CharField(max_length=100)
    paragraf = models.TextField()
    date = models.DateTimeField(default=timezone.now())
    link = models.CharField(max_length=130)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Prime"


class ImagesPrime(models.Model):
    title = models.CharField(max_length=100, default='titlu')
    image = models.ImageField(upload_to='media')
    multiImage = models.ForeignKey(Prime, on_delete=models.CASCADE, related_name='other_images')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "ImagesPrime"


class Biography(models.Model):
    title = models.CharField(max_length=100, default='titlu')
    paragraf = models.TextField()
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Biography"


class AudioMixes(models.Model):
    title = models.CharField(max_length=100)
    url = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "AudioMixes"


class FacebookLive(models.Model):
    title = models.CharField(max_length=100)

    image = models.ImageField(upload_to='media', default='default-image.png')
    link = models.CharField(max_length=130)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "FacebookLive"






