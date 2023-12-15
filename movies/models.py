from django.db import models

class MovieData(models.Model):
    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    typ = models.CharField(max_length=200,default='action')
    image = models.ImageField(upload_to='Images/',default='Images/None/Noimg.jpg')
    
    def __str__(self):
        return self.name

