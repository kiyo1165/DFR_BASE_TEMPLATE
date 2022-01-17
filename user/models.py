from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from config import settings

def upload_avater_path(instance, filename):
    ext = filename.split('.')[-1]
    return '/'.join(['avaters', str(instance.user_profile.id) + str(".") + str(ext)])


class UserManager(BaseUserManager):

    def create_user(self, email, name, password=None, **extra_fields):

        if not email:
            raise ValueError('Emailアドレスは必須です。')
        user = self.model(email=self.normalize_email(email), name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=50, unique=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    # デフォルトの入力をemailに変更
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.name

class Profile(models.Model):

    GENDER_SELECT = [
        ('male', '男性'),
        ('female', '女性'),
        ('xgender', '中間'),
    ]
    user_profile = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='user_profile',
        on_delete=models.CASCADE
    )
    img = models.ImageField(blank=True, null=True, upload_to=upload_avater_path)
    gender = models.CharField(max_length=7, blank=True, null=True, choices=GENDER_SELECT, default='mail')
    age = models.CharField(max_length=3, blank=True, null=True)
    zip_code = models.CharField(max_length=7, blank=True, null=True)
    address = models.CharField(max_length=30, blank=True, null=True)
    build_name = models.CharField(max_length=30, blank=True, null=True)
    self_description = models.TextField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.user_profile.name


class Message(models.Model):
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')

    def __str__(self):
        return self.message