from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer,MovieRetrieveSerializer
from .utils import process_movie_summary


class MovieViewSet(viewsets.ViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def list(self, request):
        movies = Movie.objects.all()
        serializer = MovieRetrieveSerializer(movies, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(): 
            movie = serializer.save() 
            # TODO: Implement this to be a background task
            print("Movie Data:", movie)
            process_movie_summary(movie)

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400) 

    def retrieve(self, request, pk=None):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=404)
        serializer = MovieRetrieveSerializer(movie)
        return Response(serializer.data)


class RatingViewSet(viewsets.ViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def create(self, request, *args, **kwargs):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            movie_id = request.data.get('movie_id')
            movie = Movie.objects.filter(id=movie_id)
        
            if not movie.exists():
                return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
            
            email = request.data.get('email') 
            score = request.data.get('score')
            comments = request.data.get('comments', '')

            rating, created = Rating.objects.get_or_create(
                movie=movie.first(),
                email=email,
                comments=comments,
                defaults={'score': score}
            )

            if not created:
                rating.score = score
                rating.save()

            serializer = RatingSerializer(rating)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400) 