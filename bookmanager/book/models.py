from django.db import models

# Create your models here.
"""
1、我们的模型类需要继承自 models.Model
2、系统会自动为我们添加一个主键--id
3、字段
      字段名=model.类型（选项）
      
      字段名其实就是数据表的字段名
      
      字段名不要使用 python、mysql等关键字
      
      char(M)
      varchar(M)
      M 就是选项
"""
class BookInfo(models.Model):
    # id
    name = models.CharField(max_length=10)  # varchar(M)相当于字符长度

# 人物 先复制过来，后期讲原理
class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键约束：人物属于哪本书
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
