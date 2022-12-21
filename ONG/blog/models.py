from django.db import models
from django.contrib.auth.models import User




class Category(models.Model):
    name = models.CharField(max_length=150)# db_index = True
    slug = models.SlugField(max_length=150, unique=True)# db_index = True
    description = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)#auto_now=True

    class Meta:
        unique_together = ('slug',)
        verbose_name_plural = "categories"


class Noticias(models.Model):

    STATUS = (
        ('draft',"Draft"),
        ('publish',"Publish")
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, null=False, unique=True, unique_for_date='created_on')
    author = models.ForeignKey(User, on_delete= models.PROTECT, related_name='comment_pots')
    category = models.ForeignKey(Category, related_name='post',blank=False, null=False,default=Category, on_delete=models.SET_DEFAULT)
    excerpt = models.CharField(max_length=300, null=True)
    image = models.ImageField(upload_to='static/img/post_feature/', blank=True, null=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS, default='draft')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey(Noticias,on_delete=models.CASCADE, related_name="comment_post")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.author


