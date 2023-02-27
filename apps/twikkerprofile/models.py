from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

if settings.DEBUG:
    from apps.twikkerprofile.fields import MockCloudinaryField as CloudinaryField
else:
    from cloudinary.models import CloudinaryField

# Create your models here.
class TwikkerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)
    avatar = CloudinaryField('image', default=settings.DEFAULT_AVATAR_URL)
    dark_mode = models.BooleanField(default=True)
    biography = models.TextField(blank=True, null=True,max_length=250, verbose_name='Biografia do usuário')
    def __str__(self):
        return self.user.username


User.twikkerprofile = property(lambda u: TwikkerProfile.objects.get_or_create(user=u)[0])
