from django.db import models
#數據模型與數據庫交互的文件
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title

# 出版商
class Publisher(models.Model):
    name = models.CharField(max_length=64)  # 名稱
    addr = models.CharField(max_length=64)  # 地址
    def __str__(self):
        return self.name

# 作者分類
class Author(models.Model):
    name = models.CharField(max_length=64)  # 姓名
    sex = models.CharField(max_length=4)  # 性別
    age = models.IntegerField(default=0)  # 年齡
    tel = models.CharField(max_length=64)  # 聯絡方式
    def __str__(self):
        return self.name

# 書籍分類
class Book(models.Model):
    name = models.CharField(max_length=64, null=True)  # 名稱
    img_and_con = models.TextField()
    ISBN = models.CharField(max_length=64)  # 編號
    author = models.ManyToManyField(Author)  # 作者，添加了作者分類的作者字段 ManyToManyField多對多
    translator = models.CharField(max_length=64)  # 譯者
    date = models.DateField(blank=True)  # 出版日期 
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE) #ForeignKey 出版商可以多個書本
    status=models.CharField(max_length=10)
    def __str__(self):
        return self.name

# 用戶分類
class LmsUser(models.Model):
    username = models.CharField(max_length=32)  # 用戶名
    password = models.CharField(max_length=32)  # 密碼
    email = models.EmailField()  # 郵箱
    mobile = models.IntegerField()  # 手機
    def __str__(self):
        return self.username


