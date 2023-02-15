from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField
from django.conf import settings

# Create your models here.
class TwikkerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)
    avatar = CloudinaryField('image', default=settings.DEFAULT_AVATAR_URL)
    dark_mode = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


User.twikkerprofile = property(lambda u: TwikkerProfile.objects.get_or_create(user=u)[0])