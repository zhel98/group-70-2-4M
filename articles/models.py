from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null= True)
    
    def __str__(self) -> str:
        return self.title
    

#новая модель категория
class Category(models.Model):
    name = models.CharField(max_length=255)
    

#новая модель комменты
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=25)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
