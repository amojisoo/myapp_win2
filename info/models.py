from django.db import models

# Create your models here.
class  Info(models.Model):
    #id              = []
    name            = models.CharField( max_length=200 , blank=True , default= "")

    created         = models.DateTimeField( auto_now_add = True )
    release_data    = models.DateTimeField()

    class Meta:
        ordering = ( "name", )

    def __str__(self):
        return self.name


