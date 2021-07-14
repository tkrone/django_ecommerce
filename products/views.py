from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from .models import Product
# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello world</h1>")
    context = {"name": "Tanner"}
    return render(request, "home.html", context)

def product_detail_view(request, pk):
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        raise Http404
    #return HttpResponse(f"Product id {obj.id}")
    # if obj.content == None:
    #     return render(request, "products/detail.html", {"object": obj})
    return render(request, "products/detail.html", {"object": obj})

def product_api_detail_view(request, pk):
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({"message": "Not found"},
        status_code=404)
    return JsonResponse({"id": {obj.id}})

def product_list_view(request, *args, **kwargs):
    qs = Product.objects.all()
    context = {"object_list": qs}
    return render(request, "products/list.html", context)