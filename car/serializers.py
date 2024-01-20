import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Car


# class CarModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class CarSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    is_published = serializers.BooleanField(default=True)
    category_id = serializers.CharField()
    slug = serializers.SlugField()
    photo = serializers.ImageField()


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