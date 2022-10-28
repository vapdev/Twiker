from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class TwikkerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)
    avatar = models.ImageField(upload_to='uploads/', blank=True, null=True, default='uploads/default.png')

    def __str__(self):
        return self.user.username


User.twikkerprofile = property(lambda u: TwikkerProfile.objects.get_or_create(user=u)[0])