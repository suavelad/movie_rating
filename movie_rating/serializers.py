from rest_framework import serializers
from .models import Movie
from .utils import is_valid_year

class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__' 

    def validate(self, attrs):
        movie = Movie.objects.filter(title=attrs['title'], release_year=attrs['release_year'], country=attrs['country'], language=attrs['language'])
        if movie.exists():
            raise serializers.ValidationError('Movie already exists')
        
        if not is_valid_year(attrs['release_year']) or type(attrs['release_year']) != int:
            raise serializers.ValidationError('Invalid year')
           
        return super().validate(attrs)
    

    def create(self, validated_data):  
        return Movie.objects.create(**validated_data)


class MovieRetrieveSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()

    def get_rating(self, obj):
        ratings = obj.ratings.all()
        if ratings:
            value = sum(rating.score for rating in ratings) / len(ratings)
            return round(value, 2)
        return None
    
    class Meta:
        model = Movie
        fields = ('id', 'title', 'rating', 'summary')


class RatingSerializer(serializers.Serializer):
    movie_id = serializers.IntegerField()
    email = serializers.EmailField()
    score = serializers.IntegerField()
    comments = serializers.CharField(required=False)
    movie_title = serializers.SerializerMethodField(read_only=True)

    def get_movie_title(self, obj):
        return obj.movie.title

    def validate(self, attrs):
        if attrs['score'] not in range(1, 6):
            raise serializers.ValidationError('Score must be between 1 and 5')
        return super().validate(attrs)