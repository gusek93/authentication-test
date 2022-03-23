from django.db import models
from conf.models import BaseModel, SoftDeleteModel
from django.contrib.contenttypes.fields import GenericRelation


class ItemCategory(models.Model):
    name = models.CharField(max_length=40)
    content_type = models.CharField(max_length=50)


class BaseItem(BaseModel, SoftDeleteModel):
    kind = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    name = models.CharField(max_length=200, null=True, default=None, blank=True)
    names = GenericRelation(
        ItemCategory, related_query_name='names'
    )

    class Meta:
        db_table = 'base_items'
        ordering = ['-id']