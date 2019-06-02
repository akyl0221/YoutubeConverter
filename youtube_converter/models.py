from django.db import models


class Download(models.Model):
    url = models.URLField(verbose_name='link')
    #date_load = models.DateTimeField(auto_now_add=True, verbose_name='date_load')
    email = models.EmailField(verbose_name='email_to', default=False)

    def __str__(self):
        return self.url
