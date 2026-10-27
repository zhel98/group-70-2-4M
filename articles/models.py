from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField()
    
#create
num_1 = Article(title='title_1', text = 'text_1', rate=1)
num_1.save()
num_2 = Article.objects.create(title='title_1', text = 'text_2', rate=2)
#read
articles = Article.objects.get(id=1)
#update
articles.text = 'new text'
articles.save()
#delete
