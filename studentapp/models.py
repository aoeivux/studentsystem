# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class MyStu(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    sex = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'my_stu'
