from django.db import models

# Create your models here.
# bookid*|bookname|readnumber|classification|author|

from django.db import models
import MySQLdb
# Create your models here.
from django.db import models

# Create your models here.


class Books(models.Model):


    bookid = models.AutoField(primary_key=True)
    bookname = models.CharField(max_length=128, unique=True)
    classification = models.CharField(max_length=256)
    author = models.CharField(max_length=128)
    maxread = models.IntegerField()
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "书"
        verbose_name_plural = "书"


class Collect(models.Model):


    userid = models.ForeignKey(
        'login.User',      # 关键在这里！！
        on_delete=models.CASCADE,
    )
    bookid = models.ForeignKey(
        'Books',      # 关键在这里！！
        on_delete=models.CASCADE,
    )
    c_time = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "收藏"
        verbose_name_plural = "收藏"


class BookList(models.Model):

    listid = models.AutoField(primary_key=True)
    listtitle = models.CharField(max_length=100)
    listcontents = models.TextField()
    bookid = models.ForeignKey(
        'Books',      # 关键在这里！！
        on_delete=models.CASCADE,
    )
    c_time = models.DateTimeField()


    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "目录"
        verbose_name_plural = "目录"

