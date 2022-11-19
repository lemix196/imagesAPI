from imagesAPI.models import Thumbnail, AccountTier, Image
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, admin
from django.contrib.auth.models import User

from imagesAPI.models import ImageUser

class ImageUserInLine(admin.StackedInline):
    model = ImageUser
    can_delete = False
    verbose_name_plural = 'imageuser'

class UserAdmin(BaseUserAdmin):
    inlines = [ImageUserInLine]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Thumbnail)
admin.site.register(AccountTier)
admin.site.register(Image)