from django.db import models

# 出版商
class Publisher(models.Model):
    img = models.TextField()
    name = models.CharField(max_length=64)  # 名稱
    addr = models.CharField(max_length=64)  # 地址

    def __str__(self):
        return self.name

# 作者分類
class Author(models.Model):
    author_img = models.TextField()
    name = models.CharField(max_length=64)  # 姓名
    sex = models.CharField(max_length=4)  # 性別
    age = models.IntegerField(default=0)  # 年齡
    tel = models.CharField(max_length=64)  # 聯絡方式(twitter)
    def __str__(self):
        return self.name

# 書籍分類
class Book1(models.Model):
    book_img = models.TextField()
    name = models.CharField(max_length=64, null=True)  # 名稱
    book_con = models.TextField()  # 簡介
    ISBN = models.CharField(max_length=64)  # 編號
    author = models.ManyToManyField(Author)  # 作者（多對多）
    translator = models.CharField(max_length=64)  # 譯者
    date = models.DateField(null=True, blank=True)  # 出版日期（可為空）
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)  # 出版商
    status = models.CharField(max_length=10) # 狀態

    def __str__(self):
        return self.name


# 用戶分類
class LmssUser(models.Model):
    name = models.CharField(max_length=32)  # 用戶名
    email = models.EmailField()  # 郵箱
    phone = models.CharField(max_length=15)  # 手機號碼
    password = models.CharField(max_length=128)  # 使用CharField儲存密碼，可以使用Django的認證系统来處裡密碼

    def __str__(self):
        return self.name
