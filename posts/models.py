from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)

    select1_content = models.CharField(max_length=50)
    select1_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='select1_users', blank=True)
    image1 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    image1_thumbnail = ImageSpecField(
        source = 'image1', # 원본 ImageField 명
        processors = [ResizeToFill(200, 300)], # 처리할 작업목록
        format = 'JPEG', # 최종 저장 포맷
        options = {'quality': 60}) # 저장 옵션

    select2_content = models.CharField(max_length=50)
    select2_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='select2_users', blank=True)
    image2 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    image2_thumbnail = ImageSpecField(
        source = 'image2',
        processors = [ResizeToFill(200, 300)],
        format = 'JPEG',
        options = {'quality': 60})

