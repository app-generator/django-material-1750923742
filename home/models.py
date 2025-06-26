# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    nama_depan = models.CharField(max_length=255, null=True, blank=True)
    nama_tengah = models.CharField(max_length=255, null=True, blank=True)
    nama_belakang = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Subject(models.Model):

    #__Subject_FIELDS__
    subject_name = models.CharField(max_length=255, null=True, blank=True)
    short_name = models.CharField(max_length=255, null=True, blank=True)

    #__Subject_FIELDS__END

    class Meta:
        verbose_name        = _("Subject")
        verbose_name_plural = _("Subject")


class User(models.Model):

    #__User_FIELDS__
    user_id = models.IntegerField(null=True, blank=True)

    #__User_FIELDS__END

    class Meta:
        verbose_name        = _("User")
        verbose_name_plural = _("User")



#__MODELS__END
