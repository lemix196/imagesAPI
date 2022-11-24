from django.test import TestCase
import pytest
from django.contrib.auth.models import User
from imagesAPI.models import Thumbnail, AccountTier, ImageUser, Image
import django.core.exceptions as dce

class ThumbnailTestCase(TestCase):
    def setUp(self):
        Thumbnail.objects.create(th_height=100)
        Thumbnail.objects.create(th_height=2000)
        Thumbnail.objects.create(th_height=999)
        Thumbnail.objects.create(th_height=1)
        Thumbnail.objects.create(th_height=-300)
        Thumbnail.objects.create(th_height=2010)


    def test_thumbnail_value_validators(self):
        th1 = Thumbnail.objects.get(th_height=100)
        th2 = Thumbnail.objects.get(th_height=2000)
        th3 = Thumbnail.objects.get(th_height=999)
        th4 = Thumbnail.objects.get(th_height=1)
        self.assertEqual(th1.th_height, 100)
        self.assertEqual(th2.th_height, 2000)
        self.assertEqual(th3.th_height, 999)
        self.assertEqual(th4.th_height, 1)

    
    def test_min_thumbnail_validator(self):
        th = Thumbnail.objects.get(th_height=-300)
        with pytest.raises(dce.ValidationError):
            th.full_clean()


    def test_max_thumbnail_validator(self):
        th = Thumbnail.objects.get(th_height=2010)
        with pytest.raises(dce.ValidationError):
            th.full_clean()


class ImageUserTestCase(TestCase):
    def setUp(self):
        th_200 = Thumbnail.objects.create(th_height=200)
        th_400 = Thumbnail.objects.create(th_height=400)
        premium_tier = AccountTier.objects.create(tier_name='Premium', is_original_allowed=False)
        premium_tier.tier_thumbnails.add(th_200)
        premium_tier.tier_thumbnails.add(th_400)
        user = User.objects.create_user('John', 'john@johnson.com', 'okmijn123')
        ImageUser.objects.create(user=user, tier=premium_tier)

    def test_tier_assignment(self):
        john = ImageUser.objects.get(id=1)
        premium_tier = AccountTier.objects.get(id=1)
        self.assertEqual(john.tier, premium_tier)
        

