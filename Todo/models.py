from django.db import models


class todoMaster(models.Model):
    content = models.CharField(blank=False, max_length=250)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.content, self.created_on)

    class Meta:
        verbose_name_plural = 'Todo Master Db'
