from django.db import models


class Download(models.Model):
    url = models.URLField(verbose_name='link')
