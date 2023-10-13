from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *
from .utils import *
# Create your views here.



class CarHome(DataMixin, ListView):
    model = Car
    template_name = 'car/index.html'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Car.objects.filter(is_published=True)

# def index(request):
#     post = Car.objects.all()
#     context = {'post': post,
#                'title': 'Glavnaya stranica',
#                "menu": menu,
#     }
#     return render(request, 'car/index.html',context=context)

def about(request):
    return render(request, 'car/about.html')

def categories(request, bmw):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{bmw}</p> ")

# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     return render(request, 'car/addpage.html', {'form': form, 'menu': menu, 'title': 'добавление статьи'})

def contact(request):
    return HttpResponse("contact")

def login(request):
    return HttpResponse("login")

def show_category(request, cat_id):
    return HttpResponse(f"category id={cat_id}")

# def show_post(request, post_id):
#     post = get_object_or_404(Car, pk=post_id)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.cat_id,
#         'cat_selected': 1,
#     }
#     return render(request, 'car/post.html', context=context)

class ShowPost(DataMixin, DetailView):
    model = Car
    template_name = 'car/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        return context


class AddPage(DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'car/addpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        context['menu'] = menu
        return context