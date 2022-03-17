from rest_framework import serializers

from .models import Article


class Article_serializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'email']


# class Article_serializer(serializers.Serializer):
#     title = serializers.CharField(max_length=100)
#     author = serializers.CharField(max_length=100)
#     email = serializers.EmailField(max_length=100)
#     date = serializers.DateTimeField()

#     def create(self, validated_data):
#         return Article.objects.create(validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.author = validated_data.get('author', instance.author)
#         instance.email = validated_data.get('email', instance.email)
#         instance.date = validated_data.get('date', instance.date)
#         return super().update(instance, validated_data)
#         instance.save()
#         return instance