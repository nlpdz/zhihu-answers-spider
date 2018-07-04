# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class baoxian(models.Model):
    bio = models.TextField(max_length=100, null=True)
    description = models.TextField(max_length=100, null=True)
    answer_count = models.IntegerField(null=True)
    zhihu_url = models.CharField(max_length=100, null=True)
    public_answer_count = models.IntegerField(null=True)
    user_id = models.CharField(max_length=100, null=True)
    user_name = models.TextField(max_length=100, null=True)
    gender = models.IntegerField(null=True)
    avatar_url = models.CharField(max_length=100, null=True)
    question_price = models.IntegerField(null=True)
    follower_count = models.IntegerField(null=True)


class chuangye(models.Model):
    bio = models.TextField(max_length=100, null=True)
    description = models.TextField(max_length=100, null=True)
    answer_count = models.IntegerField(null=True)
    zhihu_url = models.CharField(max_length=100, null=True)
    public_answer_count = models.IntegerField(null=True)
    user_id = models.CharField(max_length=100, null=True)
    user_name = models.TextField(max_length=100, null=True)
    gender = models.IntegerField(null=True)
    avatar_url = models.CharField(max_length=100, null=True)
    question_price = models.IntegerField(null=True)
    follower_count = models.IntegerField(null=True)


class dianyan(models.Model):
    bio = models.TextField(max_length=100, null=True)
    description = models.TextField(max_length=100, null=True)
    answer_count = models.IntegerField(null=True)
    zhihu_url = models.CharField(max_length=100, null=True)
    public_answer_count = models.IntegerField(null=True)
    user_id = models.CharField(max_length=100, null=True)
    user_name = models.TextField(max_length=100, null=True)
    gender = models.IntegerField(null=True)
    avatar_url = models.CharField(max_length=100, null=True)
    question_price = models.IntegerField(null=True)
    follower_count = models.IntegerField(null=True)


class ertongjiaoyu(models.Model):
    bio = models.TextField(max_length=100, null=True)
    description = models.TextField(max_length=100, null=True)
    answer_count = models.IntegerField(null=True)
    zhihu_url = models.CharField(max_length=100, null=True)
    public_answer_count = models.IntegerField(null=True)
    user_id = models.CharField(max_length=100, null=True)
    user_name = models.TextField(max_length=100, null=True)
    gender = models.IntegerField(null=True)
    avatar_url = models.CharField(max_length=100, null=True)
    question_price = models.IntegerField(null=True)
    follower_count = models.IntegerField(null=True)

class falv(models.Model):
    bio = models.TextField(max_length=100, null=True)
    description = models.TextField(max_length=100, null=True)
    answer_count = models.IntegerField(null=True)
    zhihu_url = models.CharField(max_length=100, null=True)
    public_answer_count = models.IntegerField(null=True)
    user_id = models.CharField(max_length=100, null=True)
    user_name = models.TextField(max_length=100, null=True)
    gender = models.IntegerField(null=True)
    avatar_url = models.CharField(max_length=100, null=True)
    question_price = models.IntegerField(null=True)
    follower_count = models.IntegerField(null=True)



class fangdichan(models.Model):
    bio = models.TextField(max_length=100, null=True)
    description = models.TextField(max_length=100, null=True)
    answer_count = models.IntegerField(null=True)
    zhihu_url = models.CharField(max_length=100, null=True)
    public_answer_count = models.IntegerField(null=True)
    user_id = models.CharField(max_length=100, null=True)
    user_name = models.TextField(max_length=100, null=True)
    gender = models.IntegerField(null=True)
    avatar_url = models.CharField(max_length=100, null=True)
    question_price = models.IntegerField(null=True)
    follower_count = models.IntegerField(null=True)


class jianshen(models.Model):
    bio = models.TextField(max_length=100, null=True)
    description = models.TextField(max_length=100, null=True)
    answer_count = models.IntegerField(null=True)
    zhihu_url = models.CharField(max_length=100, null=True)
    public_answer_count = models.IntegerField(null=True)
    user_id = models.CharField(max_length=100, null=True)
    user_name = models.TextField(max_length=100, null=True)
    gender = models.IntegerField(null=True)
    avatar_url = models.CharField(max_length=100, null=True)
    question_price = models.IntegerField(null=True)
    follower_count = models.IntegerField(null=True)


class licai(models.Model):
    bio = models.TextField(max_length=100, null=True)
    description = models.TextField(max_length=100, null=True)
    answer_count = models.IntegerField(null=True)
    zhihu_url = models.CharField(max_length=100, null=True)
    public_answer_count = models.IntegerField(null=True)
    user_id = models.CharField(max_length=100, null=True)
    user_name = models.TextField(max_length=100, null=True)
    gender = models.IntegerField(null=True)
    avatar_url = models.CharField(max_length=100, null=True)
    question_price = models.IntegerField(null=True)
    follower_count = models.IntegerField(null=True)


class lvyou(models.Model):
    bio = models.TextField(max_length=100, null=True)
    description = models.TextField(max_length=100, null=True)
    answer_count = models.IntegerField(null=True)
    zhihu_url = models.CharField(max_length=100, null=True)
    public_answer_count = models.IntegerField(null=True)
    user_id = models.CharField(max_length=100, null=True)
    user_name = models.TextField(max_length=100, null=True)
    gender = models.IntegerField(null=True)
    avatar_url = models.CharField(max_length=100, null=True)
    question_price = models.IntegerField(null=True)
    follower_count = models.IntegerField(null=True)


class meishi(models.Model):
    bio = models.TextField(max_length=100, null=True)
    description = models.TextField(max_length=100, null=True)
    answer_count = models.IntegerField(null=True)
    zhihu_url = models.CharField(max_length=100, null=True)
    public_answer_count = models.IntegerField(null=True)
    user_id = models.CharField(max_length=100, null=True)
    user_name = models.TextField(max_length=100, null=True)
    gender = models.IntegerField(null=True)
    avatar_url = models.CharField(max_length=100, null=True)
    question_price = models.IntegerField(null=True)
    follower_count = models.IntegerField(null=True)

class qiche(models.Model):
    bio = models.TextField(max_length=100, null=True)
    description = models.TextField(max_length=100, null=True)
    answer_count = models.IntegerField(null=True)
    zhihu_url = models.CharField(max_length=100, null=True)
    public_answer_count = models.IntegerField(null=True)
    user_id = models.CharField(max_length=100, null=True)
    user_name = models.TextField(max_length=100, null=True)
    gender = models.IntegerField(null=True)
    avatar_url = models.CharField(max_length=100, null=True)
    question_price = models.IntegerField(null=True)
    follower_count = models.IntegerField(null=True)


class sheying(models.Model):
    bio = models.TextField(max_length=100, null=True)
    description = models.TextField(max_length=100, null=True)
    answer_count = models.IntegerField(null=True)
    zhihu_url = models.CharField(max_length=100, null=True)
    public_answer_count = models.IntegerField(null=True)
    user_id = models.CharField(max_length=100, null=True)
    user_name = models.TextField(max_length=100, null=True)
    gender = models.IntegerField(null=True)
    avatar_url = models.CharField(max_length=100, null=True)
    question_price = models.IntegerField(null=True)
    follower_count = models.IntegerField(null=True)


class shijianguanli(models.Model):
    bio = models.TextField(max_length=100, null=True)
    description = models.TextField(max_length=100, null=True)
    answer_count = models.IntegerField(null=True)
    zhihu_url = models.CharField(max_length=100, null=True)
    public_answer_count = models.IntegerField(null=True)
    user_id = models.CharField(max_length=100, null=True)
    user_name = models.TextField(max_length=100, null=True)
    gender = models.IntegerField(null=True)
    avatar_url = models.CharField(max_length=100, null=True)
    question_price = models.IntegerField(null=True)
    follower_count = models.IntegerField(null=True)

class shipinanquan(models.Model):
    bio = models.TextField(max_length=100, null=True)
    description = models.TextField(max_length=100, null=True)
    answer_count = models.IntegerField(null=True)
    zhihu_url = models.CharField(max_length=100, null=True)
    public_answer_count = models.IntegerField(null=True)
    user_id = models.CharField(max_length=100, null=True)
    user_name = models.TextField(max_length=100, null=True)
    gender = models.IntegerField(null=True)
    avatar_url = models.CharField(max_length=100, null=True)
    question_price = models.IntegerField(null=True)
    follower_count = models.IntegerField(null=True)

class shishang(models.Model):
    bio = models.TextField(max_length=100, null=True)
    description = models.TextField(max_length=100, null=True)
    answer_count = models.IntegerField(null=True)
    zhihu_url = models.CharField(max_length=100, null=True)
    public_answer_count = models.IntegerField(null=True)
    user_id = models.CharField(max_length=100, null=True)
    user_name = models.TextField(max_length=100, null=True)
    gender = models.IntegerField(null=True)
    avatar_url = models.CharField(max_length=100, null=True)
    question_price = models.IntegerField(null=True)
    follower_count = models.IntegerField(null=True)


class xinlixue(models.Model):
    bio = models.TextField(max_length=100, null=True)
    description = models.TextField(max_length=100, null=True)
    answer_count = models.IntegerField(null=True)
    zhihu_url = models.CharField(max_length=100, null=True)
    public_answer_count = models.IntegerField(null=True)
    user_id = models.CharField(max_length=100, null=True)
    user_name = models.TextField(max_length=100, null=True)
    gender = models.IntegerField(null=True)
    avatar_url = models.CharField(max_length=100, null=True)
    question_price = models.IntegerField(null=True)
    follower_count = models.IntegerField(null=True)


class yinyue(models.Model):
    bio = models.TextField(max_length=100, null=True)
    description = models.TextField(max_length=100, null=True)
    answer_count = models.IntegerField(null=True)
    zhihu_url = models.CharField(max_length=100, null=True)
    public_answer_count = models.IntegerField(null=True)
    user_id = models.CharField(max_length=100, null=True)
    user_name = models.TextField(max_length=100, null=True)
    gender = models.IntegerField(null=True)
    avatar_url = models.CharField(max_length=100, null=True)
    question_price = models.IntegerField(null=True)
    follower_count = models.IntegerField(null=True)

class yixue(models.Model):
    bio = models.TextField(max_length=100, null=True)
    description = models.TextField(max_length=100, null=True)
    answer_count = models.IntegerField(null=True)
    zhihu_url = models.CharField(max_length=100, null=True)
    public_answer_count = models.IntegerField(null=True)
    user_id = models.CharField(max_length=100, null=True)
    user_name = models.TextField(max_length=100, null=True)
    gender = models.IntegerField(null=True)
    avatar_url = models.CharField(max_length=100, null=True)
    question_price = models.IntegerField(null=True)
    follower_count = models.IntegerField(null=True)



class youxi(models.Model):
    bio = models.TextField(max_length=100, null=True)
    description = models.TextField(max_length=100, null=True)
    answer_count = models.IntegerField(null=True)
    zhihu_url = models.CharField(max_length=100, null=True)
    public_answer_count = models.IntegerField(null=True)
    user_id = models.CharField(max_length=100, null=True)
    user_name = models.TextField(max_length=100, null=True)
    gender = models.IntegerField(null=True)
    avatar_url = models.CharField(max_length=100, null=True)
    question_price = models.IntegerField(null=True)
    follower_count = models.IntegerField(null=True)

class yuyanxuexi(models.Model):
    bio = models.TextField(max_length=100, null=True)
    description = models.TextField(max_length=100, null=True)
    answer_count = models.IntegerField(null=True)
    zhihu_url = models.CharField(max_length=100, null=True)
    public_answer_count = models.IntegerField(null=True)
    user_id = models.CharField(max_length=100, null=True)
    user_name = models.TextField(max_length=100, null=True)
    gender = models.IntegerField(null=True)
    avatar_url = models.CharField(max_length=100, null=True)
    question_price = models.IntegerField(null=True)
    follower_count = models.IntegerField(null=True)

class zhiyeguihua(models.Model):
    bio = models.TextField(max_length=100, null=True)
    description = models.TextField(max_length=100, null=True)
    answer_count = models.IntegerField(null=True)
    zhihu_url = models.CharField(max_length=100, null=True)
    public_answer_count = models.IntegerField(null=True)
    user_id = models.CharField(max_length=100, null=True)
    user_name = models.TextField(max_length=100, null=True)
    gender = models.IntegerField(null=True)
    avatar_url = models.CharField(max_length=100, null=True)
    question_price = models.IntegerField(null=True)
    follower_count = models.IntegerField(null=True)






