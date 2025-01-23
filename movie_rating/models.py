from django.db import models



app_name = 'movies'

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_year = models.IntegerField()
    country = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    production_company = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    summary = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    score = models.IntegerField(choices=[(i, i) for i in range(1, 5)])
    email = models.EmailField()
    comments = models.TextField(blank=True)


    def __str__(self):
        return f"Movie titled:{self.movie.title} was rated with {self.score} stars"