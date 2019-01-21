from django.db import models

# Create your models here.
#创建一个实体类 - Publisher 表示"出版社"
#1.name:出版社名称 - varchar
#2.address:出版社地址 - varchar
#3.city:出版社所在城市 - varchar
#4.country:出版社所在国家 - varchar
#5.website:出版社网址 - varchar
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    website = models.URLField(null=True)

#创建 Author 实体类
# 1.name - 姓名(CharField() -> varchar)
# 2.age - 年龄(IntegerFiled() -> int)
# 3.email - 邮箱(EmailField() -> varchar)
class Author(models.Model):
    name = models.CharField(max_length=30,verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    email = models.EmailField(null=True,verbose_name='邮箱')
    isActive = models.BooleanField(default=True,verbose_name='有效用户')

    # 重写 __str__ 函数,以便定义对象在后台的表现名称
    def __str__(self):
        return self.name

    class Meta:
        #1.指定表名
        db_table = "author"
        #2.指定在 admin 中显示的名称
        verbose_name = '作者'
        #3.指定在 admin 中显示的名称
        verbose_name_plural = verbose_name
        #4.指定在 admin 中按照 年龄降序排序
        ordering = ['-age']

class Book(models.Model):
    title = models.CharField(max_length=50)
    publicate_date = models.DateField()

class Wife(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    #增加对Author的一对一关联关系
    author = models.OneToOneField(Author)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "wife"





