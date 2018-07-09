from django.db import models

# Create your models here.
appName = "info"

class  Info(models.Model):
    #id              = []
    name            = models.CharField( max_length=200 , blank=True , default= "")
    code            = models.CharField( max_length=200 , blank=True , default= "")
    memo            = models.CharField( max_length=200 , blank=True , default= "")

    #created         = models.DateTimeField( auto_now_add = True )
    #release_data    = models.DateTimeField( auto_now_add = True )

    class Meta:
        ordering = ( "id", )

    def __str__(self):
        return self.name

    #def get_absolute_url(self):
    #    return u'/info/%d' % ( appName , self.id )

