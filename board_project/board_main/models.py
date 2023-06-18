from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Post(models.Model):
    title = models.CharField(max_length = 100)
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # DB에는 fk를 설정한 변수명에 _id 가 붙게 된다
    # on_delete = models.CASCADE,
    # db에 author_id는 파이썬에서는 author 겍체와 같은 것.
    author = models.ForeignKey(Author, on_delete = models.SET_NULL, null = True, related_name = 'posts' )


