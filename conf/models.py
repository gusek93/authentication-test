from django.db import models
from django.utils import timezone


class SoftDeleteManager(models.Manager):
    use_for_related_field = True
    
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        super(SoftDeleteManager, self).__init__(*args, **kwargs)
        
    def get_queryset(self):
        if not self.alive_only:
            return super().get_queryset()
        return super().get_queryset().filter(deleted_at__isnull=True)
    
    def hard_delete(self):
        return self.get_queryset().hard_delete()
    
    
class SoftDeleteModel(models.Model):
    
    deleted_at = models.DateTimeField('삭제일', null=True, default=None)
    
    class Meta:
        abstract = True
        
    objects = SoftDeleteManager()
    include = SoftDeleteManager(alive_only=False)
    
    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save(update_fields=['deleted_at'])
        
    def restore(self):
        self.deleted_at = None
        self.save(update_fields=['deleted-at'])
        
    def hard_delete(self):
        super(SoftDeleteModel, self).delete()
        

class BaseModel(models.Model):
    created_at = models.DateTimeField('등록일', auto_now_add=True)
    updated_at = models.DateTimeField('수정일', auto_now=True)
    
    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']