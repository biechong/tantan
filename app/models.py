from django.db import models

class User(models.Model):
    phonenum = models.IntegerField()
    nickname = models.CharField(max_length=20)
    sex = models.BooleanField()
    birth_year = models.IntegerField()
    birth_month = models.IntegerField()
    birth_day = models.IntegerField()
    avatar = models.CharField(max_length=400)
    location = models.CharField(max_length=200)
    def __str__(self):
        return "%s"%self.name
    class Meta:
        db_table = "users"

class Profile(models.Model):
    location = models.CharField(max_length=200)
    min_distance = models.CharField(max_length=200)
    max_distance = models.CharField(max_length=200)
    min_dating_age = models.IntegerField()
    max_dating_age = models.IntegerField()
    dating_sex = models.BooleanField()
    virbration = models.BooleanField()
    only_matche = models.BooleanField()
    auto_play = models.BooleanField()
    user = models.OneToOneField("IdUser", on_delete=models.CASCADE)
    def __str__(self):
        return "%s"%self.name
    class Meta:
        #对应数据中的表名
        db_table = "profiles"