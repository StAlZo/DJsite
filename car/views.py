# from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponse
# from django.urls import reverse_lazy
# from django.views.generic import ListView, DetailView, CreateView
#
# from .forms import *
from django.forms import model_to_dict
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import *
# from .utils import *
# Create your views here.
from rest_framework import generics, viewsets

from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import CarSerializer, CarSerializ, CarSeriali
from rest_framework.views import APIView
from rest_framework.response import Response


class CarApi(generics.ListAPIView):
    """2-3 video"""
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarAPIView(APIView):
    """4 video"""
    def get(self, requests):
        lst = Car.objects.all()
        return Response({'posts': CarSerializer(lst, many=True).data})

    def post(self, requests):
        serializer = CarSerializer(data=requests.data)
        serializer.is_valid(raise_exception=True)

        post_new = Car.objects.create(
            title=requests.data['title'],
            content=requests.data['content'],
            category_id=requests.data['cat_id']
        )
        return Response({'post': CarSerializer(post_new).data})


class CarAP(APIView):
    """5 video"""
    def get(self, requests):
        lst = Car.objects.all()
        return Response({'posts': CarSerializ(lst, many=True).data})

    def post(self, requests):
        serializer = CarSerializ(data=requests.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def put(self,requests, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUD syety navel"})
        try:
            instance = Car.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = CarSerializ(data=requests.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})


class CarA(APIView):
    """6 video"""
    def get(self, requests):
        lst = Car.objects.all()
        return Response({'posts': CarSeriali(lst, many=True).data})

    def post(self, requests):
        serializer = CarSeriali(data=requests.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def put(self, requests, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUD syety navel"})
        try:
            instance = Car.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = CarSeriali(data=requests.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})


class CarAPIList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSeriali


class CarAPIUpdate(generics.UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSeriali
    premission_clases = (IsOwnerOrReadOnly, )


class CarAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSeriali
    premission_classes = (IsAdminOrReadOnly,)


class CarViewSet(viewsets.ModelViewSet):
    """8 video"""
    queryset = Car.objects.all()
    serializer_class = CarSeriali
    premission_classes = (IsAdminOrReadOnly,)


class CarViewSet1(viewsets.ModelViewSet):
    """9 video"""
    #queryset = Car.objects.all()
    serializer_class = CarSeriali
    premission_classes = (IsAdminOrReadOnly, IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly)


    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if not pk:
            return Car.objects.all()

        return Car.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def category(self, requests, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})

# class CarAPIView(generics.ListAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer

# class CarHome(DataMixin, ListView):
#     model = Car
#     template_name = 'car/index.html'
#     context_object_name = 'posts'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title="Главная страница")
#         return dict(list(context.items()) + list(c_def.items()))
#
#     def get_queryset(self):
#         return Car.objects.filter(is_published=True)
#
# # def index(request):
# #     post = Car.objects.all()
# #     context = {'post': post,
# #                'title': 'Glavnaya stranica',
# #                "menu": menu,
# #     }
# #     return render(request, 'car/index.html',context=context)
#
# def about(request):
#     return render(request, 'car/about.html')
#
# def categories(request, bmw):
#     return HttpResponse(f"<h1>Статьи по категориям</h1><p>{bmw}</p> ")
#
# # def addpage(request):
# #     if request.method == 'POST':
# #         form = AddPostForm(request.POST, request.FILES)
# #         if form.is_valid():
# #             form.save()
# #             return redirect('home')
# #     else:
# #         form = AddPostForm()
# #     return render(request, 'car/addpage.html', {'form': form, 'menu': menu, 'title': 'добавление статьи'})
#
# def contact(request):
#     return HttpResponse("contact")
#
# def login(request):
#     return HttpResponse("login")
#
# def show_category(request, cat_id):
#     return HttpResponse(f"category id={cat_id}")
#
# # def show_post(request, post_id):
# #     post = get_object_or_404(Car, pk=post_id)
# #
# #     context = {
# #         'post': post,
# #         'menu': menu,
# #         'title': post.cat_id,
# #         'cat_selected': 1,
# #     }
# #     return render(request, 'car/post.html', context=context)
#
#
# class ShowPost(DataMixin, DetailView):
#     model = Car
#     template_name = 'car/post.html'
#     slug_url_kwarg = 'post_slug'
#     context_object_name = 'post'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = context['post']
#         context['menu'] = menu
#         return context
#
#
# class AddPage(DataMixin, CreateView):
#     form_class = AddPostForm
#     template_name = 'car/addpage.html'
#     success_url = reverse_lazy('home')
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Добавление статьи'
#         context['menu'] = menu
#         return context

