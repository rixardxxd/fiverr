from django.db import models

# Create your models here.

class Gig(models.Model):
    class Meta:
        verbose_name = ""

    gig_id = models.AutoField(primary_key=True)
    seller_id = models.ForeignKey('User')
    rating_avg = models.FloatField(default=0.0)
    rating_count = models.IntegerField(default=0)


    def __unicode__(self):
        return u'gig_id: {} ____ seller_id: {} ____ rating_avg: {} ____ rating_count: {}'.format(self.name, self.price, self.size, self.city, self.img)

