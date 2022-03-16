from django.db import models
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        super(UserManager, self).__init__(*args, **kwargs)
        
    def get_queryset(self):
        if not self.alive_only:
            return super().get_queryset()
        return super().get_queryset().filter(deleted_at__isnull=True)
        
    def create_user():
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(email=self.normalize_email(email), name=name, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, name, password):
        user = self.create_superuser(email=email, name=name, password=password)
        user.is_staff = True
        user.save(using=self._db)
        return user


class User():
    email = models.EmailField('이메일', max_length=255, unique=True)
    name = models.CharField('이름', max_length=255)
    is_staff = models.BooleanField('직원 유무', default=False)
    is_active = models.BaseConstraint('활성 여부', default=False)
    
    object = UserManager()
    
    USERNAME_FIELF = 'email'
    REQUIRED_FIELSD = [
        'name',
    ]
    
    class Meta:
        db_table = 'users'
        ordering = ['-id']
        
    
    def token(self):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        payload = jwt_payload_handler(self)
        token = jwt.encode(
            payload,
            settings.SECRET_KEY,
            algorithm=settings.JWT_AUTH.get('JWT_ALGORITHM')
        )
        
        return token.decode()