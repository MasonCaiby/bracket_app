from django.db import models
from django.template.defaultfilters import slugify

class ActiveTeam(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    link = models.TextField()
    prev_score = models.IntegerField()
    round_number = models.IntegerField()
    rank = models.IntegerField()
    #image = models.ImageField(upload_to ='uploads/')

    def __str__(self):
        return f"active: {self.title}-{self.round_number}"

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(f"{self.title} {self.round_number}")

        super(ActiveTeam, self).save(*args, **kwargs)
