from django.db import models

# Create your models here.
class Tree(models.Model):
    name = models.CharField(max_length = 100, blank = True, default = '')
    creation_time = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ('creation_time',)
