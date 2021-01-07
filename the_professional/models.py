from django.db import models
from PIL import Image as i
# Create your models here.


class BackEndSkills(models.Model):
    name = models.CharField(max_length=100)
    percent = models.IntegerField()

    class Meta:
        verbose_name_plural = "BackEndSkills"

    def __str__(self):
        template = '{0.name} {0.percent}'
        return template.format(self)


class SoftSkills(models.Model):
    name = models.CharField(max_length=100)
    percent = models.IntegerField()

    class Meta:
        verbose_name_plural = "SoftSkills"

    def __str__(self):
        template = '{0.name} {0.percent}'
        return template.format(self)


class Services(models.Model):
    title = models.CharField(max_length=100)
    paragraph = models.TextField()

    class Meta:
        verbose_name_plural = "Services"

    def __str__(self):
        return self.title


class Projects(models.Model):
    title = models.CharField(max_length=100)
    paragraph = models.TextField()
    link = models.TextField()
    image_project = models.ImageField(upload_to='media', verbose_name='Image')

    class Meta:
        verbose_name_plural = "Projects"

    def save(self, *args, **kwargs):
        super(Projects, self).save(*args, **kwargs)

        img = i.open(self.image_project.path)
        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image_project.path)

    def __str__(self):
        return self.title


class Counter(models.Model):
    number = models.IntegerField()
    speed = models.IntegerField()
    achieved_goal = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Counter"

    def __str__(self):
        template = '{0.achieved_goal} {0.number}'
        return template.format(self)


class IntroductionCv(models.Model):
    paragraph = models.TextField()
    pdf = models.FileField(upload_to='media', verbose_name='PDF')

    def __str__(self):
        template = '{0.paragraph} {0.pdf}'
        return template.format(self)

    class Meta:
        verbose_name_plural = "Introduction Cv"