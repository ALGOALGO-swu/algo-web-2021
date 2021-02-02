# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Map(models.Model):
    feature = models.IntegerField()
    ahead_to = models.IntegerField()
    baekjoon_no = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'map'


class Member(models.Model):
    discord_id = models.CharField(unique=True, max_length=45)
    student_id = models.CharField(unique=True, max_length=45)
    name = models.CharField(max_length=45)
    point = models.IntegerField()
    map_location = models.IntegerField()
    status = models.IntegerField()
    items = models.TextField(blank=True, null=True)
    daily_steps = models.IntegerField(blank=True, null=True)
    baekjoon_id = models.CharField(max_length=45, blank=True, null=True)
    bj_solved = models.TextField(blank=True, null=True)
    bj_solv_contd = models.IntegerField()
    bj_rank = models.CharField(max_length=45, blank=True, null=True)
    bj_today = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'member'
