import datetime

from django.db import models
from django.utils.functional import cached_property


class User(models.Model):
    SEX = (
        ('男', '男'),
        ('女', '女'),
    )
    # 昵称  电话  性别
    nickname = models.CharField(max_length=32, unique=True)
    phonenum = models.CharField(max_length=16, unique=True)
    sex = models.CharField(max_length=8, choices=SEX)
    # 个人形象  常居地
    avatar = models.CharField(max_length=256)
    location = models.CharField(max_length=32)
    # 用户年月日
    birth_year = models.IntegerField(default=2000)
    birth_month = models.IntegerField(default=1)
    birth_day = models.IntegerField(default=1)

    # 年龄
    @cached_property
    def age(self):
        today = datetime.date.today()
        birth_date = datetime.date(self.birth_year, self.birth_month, self.birth_day)
        times = today - birth_date
        return times.days // 365

    @property
    def profield(self):
        '''
        用户配置项
        做关联
        懒加载
        '''
        if not hasattr(self, '_profile'):
            self._profile, _ = Profile.objects.get_or_create(id=self.id)
        return self._profile

    # self.profile.location
    # self.profile.min_dating_age
    # self.profile.max_distance


class Profile(models.Model):
    '''用户配置项'''
    SEX = (
        ('男', '男'),
        ('女', '女'),
    )
    dating_sex = models.CharField(default='男', max_length=8, choices=SEX, verbose_name="匹配性别")
    location = models.CharField(max_length=32, verbose_name="目标城市")

    min_distance = models.IntegerField(default=1, verbose_name="最大查找范围")
    max_distance = models.IntegerField(default=10, verbose_name="最小查找范围")

    min_dating_age = models.IntegerField(default=18, verbose_name="最小交友年龄")
    max_dating_age = models.IntegerField(default=45, verbose_name="最大交友年龄")

    vibration = models.BooleanField(default=True, verbose_name="开启振动")
    only_matche = models.BooleanField(default=True, verbose_name="不让未匹配的人看到我的相册")
    auto_play = models.BooleanField(default=True, verbose_name="自动播放视频")
