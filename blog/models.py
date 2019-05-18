from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=30)
    pub_date = models.DateField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/blog')

    def __str__(self):
        return self.title

    def blogsummary(self):
        return self.body[:50]+'...'

    def modifieddate(self):
        return self.pub_date.strftime('%A, %B %d')
