from django.db import models

# Create your models here.
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length =50, default="")
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.title