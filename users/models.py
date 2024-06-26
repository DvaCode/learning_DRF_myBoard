from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nickname = models.CharField(max_length=120)
    position = models.CharField(max_length=120)
    subjects = models.CharField(max_length=120)
    image = models.ImageField(upload_to='profile/', default='default.png')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    '''
    User 모뎅리 post_save 이벤트를 발생시켰을 때 해당 이벤트가 일어났다는 사실을 받아서,
    해당 유저의 인스턴스와 연결되는 프로필 데이터를 생성합니다. @receiver 덕분에 프로필 생성해 주는 코드
    직접 작성하지 않아도 알아서 유저 생성 이벤트를 감지해 프로필을 자동으로 생성할 수 있음
    '''
    if created:
        Profile.objects.create(user=instance)