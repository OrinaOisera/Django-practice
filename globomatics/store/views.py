from django.core.paginator import Paginator, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views import View
from django.urls import path

# Create your views here.
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.gzip import gzip_page
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView, ListView


def index(request):
    return HttpResponse("Hello this is a store ")


def detail(request):
    return HttpResponse("Hello there globomatics is an ecommerce  store for all thingdselectronic")


@csrf_exempt
@cache_page(900)
@gzip_page
@require_http_methods(["GET"])
def electronics(request):
    items = ("Windows", "Mac", "Lenovo", "Acer", "Dell", "Samsung")
    if request.method == "GET":
        paginator = Paginator(items, 2)
        pages = request.GET.get('page', 1)
        try:
            items = paginator.page(pages)
        except PageNotAnInteger:
            items = paginator.page(1)
        response = render(request, 'store/list.html', {'items': items})
        if request.COOKIES.get('visits'):
            value = int(request.COOKIES.get('visits'))
            print("Getting cookies")
            print(value)
            response.set_cookie('visits', value + 1)
        else:
            value = 1
            print("Setting cookie")
            # breakpoint()
            # response.set_cookie('visits', value)

    elif request.method == 'POST':
        return HttpResponseNotFound("This is not allowed")


class ElectronicsView(View):
    def get(self, request):
        items = ("Windows", "Mac", "Lenovo", "Acer", "Dell", "Samsung")
        paginator = Paginator(items, 2)
        pages = request.GET.get('page', 1)
        self.process()
        try:
            items = paginator.page(pages)
        except PageNotAnInteger:
            items = paginator.page(1)
        return render(request, 'store/list1.html', {'items': items})

    def process(self):
        print("We are processing Electronics")


class ElectronicsView2(TemplateView):
    template_name = 'store/list.html'

    def get_context_data(self, **kwargs):
        items = ("Windows", "Mac", "Lenovo", "Acer", "Dell", "Samsung")
        context = {'items': items}
        return context


class ElectronicsView3(ListView):
    template_name = 'store/list1.html'
    queryset = ("Windows", "Mac", "Lenovo", "Acer", "Dell", "Samsung445")
    context_object_name = 'items'
    paginate_by = 2


class ComputersView(ElectronicsView):
    def process(self):
        print("We are processing computers")


class MobileView():
    def process(self):
        print("We are processing Mobilephones")


class EquipmentView(MobileView, ComputersView):
    pass

