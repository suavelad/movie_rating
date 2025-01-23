from django.test import TestCase
from .models import Movie

from django.test import TestCase
from rest_framework.test import APIClient
from .models import Movie
from .serializers import MovieSerializer

class MovieAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.movie_data = {
            'title': 'The Shawshank Redemption',
            'release_year': 1994,
            'country': 'USA',
            'language': 'English'
        }

    def test_create_movie(self):
        response = self.client.post('/movies/', self.movie_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['title'], 'The Shawshank Redemption')

    def test_get_movie_list(self):
        self.client.post('/movies/', self.movie_data, format='json')
        response = self.client.get('/movies/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'The Shawshank Redemption')

    def test_get_single_movie(self):
        movie = Movie.objects.create(**self.movie_data)
        response = self.client.get(f'/movies/{movie.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'The Shawshank Redemption')

    def test_create_movie_with_invalid_data(self):
        invalid_data = {
            'release_year': 'invalid_year' 
        }
        response = self.client.post('/movies/', invalid_data, format='json')
        self.assertEqual(response.status_code, 400) 

    def test_get_non_existent_movie(self):
        response = self.client.get('/movies/999/')
        self.assertEqual(response.status_code, 404)

        

  