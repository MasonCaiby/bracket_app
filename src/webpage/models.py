from django.db import models

# Create your models here.

# Create your models here.
class ActiveTeam(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    link = models.TextField()
    score = models.IntegerField()
    round_number = models.IntegerField()
    #image = models.ImageField(upload_to ='uploads/')

    def __str__(self):
        return f"active: {self.title}-{self.round_number}"
