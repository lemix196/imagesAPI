from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Thumbnail(models.Model):
    """Model class for storing Thumbnail heights. Has one field with int value of 
       thumbnail height and is in Many-To-Many relationship with AccountTier model class.
       
            th_height [int]: integer value of thumbnail height (in pixels) fron range 1 to 2000"""

    th_height = models.IntegerField(primary_key=True, validators=[MaxValueValidator(2000), 
                                                                  MinValueValidator(1)])

    def __str__(self):
        return str(self.th_height)


class AccountTier(models.Model):
    """Model class for storing tier name, thumbnail height values accessible for 
       that tier and data about permission to original sized image.
       
            tier_name [django.models.CharField]: user tier name, maximum length of 30 characters,
            tier_thumbnails [django.models.ManyToManyField]: Many-To_Many relation between tables
                                                            Thumbnail and AccountTier,
            is_original_allowed [django.models.BooleanField]: bool value allowing access to original
                                                              size of uploaded image if True"""
    tier_name = models.CharField(max_length=30)
    tier_thumbnails = models.ManyToManyField(Thumbnail, blank=False, null=False)
    is_original_allowed = models.BooleanField()

    def __str__(self):
        return self.tier_name


class ImageUser(models.Model):
    """Model class overriding built-in Django User and adding tier to every user created (obligatory)."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tier = models.ForeignKey(AccountTier, on_delete=models.CASCADE, blank=False, null=False)


class Image(models.Model):
    img = models.ImageField()
    original_url = models.CharField(max_length=200, blank=True, null=True)
    thumbnail_urls = models.JSONField(blank=True, null=True)
    owner = models.ForeignKey('auth.User', related_name='images', on_delete=models.CASCADE, blank=False, null=False)


    def save(self, *args, **kwargs):
        if not self.original_url:
            # generate link to original-sized image
            next_id = Image.objects.latest('id').id + 1
            self.original_url = 'api/images/{}'.format(next_id)

        if not self.thumbnail_urls:
            # generate urls for thumbnail images
            thumbnail_height_values = self.owner.imageuser.tier.tier_thumbnails.values()
            th_dict = {}
            next_id = Image.objects.latest('id').id + 1
            for ind, value in enumerate(thumbnail_height_values):
                value = list(value.values())[0]
                th_dict[ind] = 'api/images/{}/{}'.format(next_id, value)
            self.thumbnail_urls = th_dict

        return super(Image, self).save(*args, **kwargs)
