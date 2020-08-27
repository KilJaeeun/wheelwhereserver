from django.db import models

# Create your models here.
class post(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    address =models.TextField(blank=True, default="")
    phone = models.CharField(max_length =255, null =True, blank=True)
    is_toilet = models.BooleanField(default=False)
    is_elivator = models.BooleanField(default=False)
    is_parking= models.BooleanField(default=False)
    is_tuck= models.BooleanField(default=False)
    is_helper= models.BooleanField(default=False)

   # oldAddress=models.TextField(blank=True, default="")

    description = models.TextField()
    latitude = models.CharField(max_length=255,  default=0)
    longitude = models.CharField(max_length=255, default=0)
    star = models.FloatField(null=True, default=0)
    author =models.ForeignKey('user.user', on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']

    def get_field_names(self):
        meta = self._meta
        field_names = ([field.name for field in meta.fields])
        return field_names

class comment(models.Model):
    post = models.ForeignKey(post, on_delete=models.CASCADE, null=True)
    text = models.TextField()
    author = models.ForeignKey('user.user', on_delete=models.CASCADE, null=True)
    star = models.FloatField(null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-created_at']

    def get_field_names(self):
        meta = self._meta
        field_names = ([field.name for field in meta.fields])
        return field_names
    def save(self, *args, **kwargs):
        if self.post:
            self.post.save()

        super(comment, self).save(*args, **kwargs)
