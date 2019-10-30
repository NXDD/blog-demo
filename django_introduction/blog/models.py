from django.db import models

# Create your models here.


class Article(models.Model):
    # 文章的唯一ID
    article_id = models.AutoField(primary_key=True)
    # 文章标题
    title = models.TextField()
    # 文章摘要
    brief_content = models.TextField()
    # 文章的主要内容
    content = models.TextField()
    # 文章的发布日期
    publish_date = models.DateTimeField(auto_now=True)  # 默认当前时间为文章发布时间

    def __str__(self):
        return self.title  # 文章名字从django自定义变成了我们自己设定的title
