import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Car


class CarModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content


class CarSer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = {'title', 'category_id'}


class CarSerializer(serializers.Serializer):
    """4 video"""
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    is_published = serializers.BooleanField(default=True)
    category_id = serializers.CharField()
    slug = serializers.SlugField()
    photo = serializers.ImageField()


class CarSerializ(serializers.Serializer):
    """5 video"""
    title = serializers.CharField(max_length=255)
    content = serializers.CharField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    category_id = serializers.CharField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    photo = serializers.ImageField(read_only=True)

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.is_published = validated_data.get("is_published", instance.is_published)
        instance.category_id = validated_data.get("category_id", instance.category_id)
        instance.slug = validated_data.get("slug", instance.slug)
        instance.photo = validated_data.get("photo", instance.photo)
        instance.save()
        return instance


class CarSeriali(serializers.ModelSerializer):
    """6 video"""
    class Meta:
        model = Car
        fields = ("title", "content", "category_id", "slug")

# def encode():
#     model = CarModel('e39', 'pizda che za tachka')
#     model_sr = CarSerializer(model)
#     json = JSONRenderer().render(model_sr.data)
#
# def decode():
#     stream = io.BytesIO(b'{"title":"e39", "content":"pizda che za tachka"')
#     data = JSONParser().parse(stream)
#     serializers = CarSerializer(data)
#     serializers.is_valid()