from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    User
)
from pub.models import Pub
from PIL import Image


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have email')
        if not password:
            raise ValueError('Users must have password')

        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email, password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name='email address'
    )
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=75, null=True)
    image = models.ImageField(
        default='profile_pics/default.jpg', upload_to='profile_pics', null=True)
    favorites = models.ManyToManyField(
        Pub, related_name='favorited_by', null=True)

    def __str__(self):
        return f'{self.user.email} Profile'

    def save(self, force_insert=False, force_update=False, using=None):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


# def create_profile(sender, **kwargs):
#     if kwargs['created']:
#         user_profile = Profile.objects.create(user=kwargs['instance'])
#
#
# post_save.connect(create_profile, sender=User)
