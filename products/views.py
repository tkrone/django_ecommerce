from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render, redirect

from .forms import ProductModelForm
from .models import Product

# def bad_view(request, *args, **kwargs):
#     print(dict(request.GET))
#     my_request_data= dict(request.GET)
#     new_product = my_request_data.get("new_product")
#     print(my_request_data, new_product)
#     if new_product[0].lower() == "true":
#         print("new product")
#         Product.objects.create(title=my_request_data.get('title')[0], content=my_request_data.get('content')[0])
#     return HttpResponse("Dont do this")

# Create your views here.
def search_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello world</h1>")
    query = request.GET.get('q')
    qs = Product.objects.filter(title__icontains=query[0])
    print(query, qs)
    context = {"name": "Tanner", "query": query}
    return render(request, "home.html", context)

# def product_create_view(request, *args, **kwargs):
#     # print(request.POST)
#     # print(request.GET)
#     if request.method =="POST":
#         post_data = request.POST or None
#         if post_data != None:
#             my_form = ProductForm(request.POST)
#             if my_form.is_valid():
#                 print(my_form.cleaned_data.get("title"))
#                 title_from_input = my_form.cleaned_data.get("title")
#                 Product.objects.create(title=title_from_input)
#     return render(request, "forms.html", {})

@staff_member_required
def product_create_view(request, *args, **kwargs):
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        # do some stuff
        obj.user = request.user
        obj.save()

        # print(request.POST)
        # print(form.cleaned_data) # Always use cleaned data
        # data = form.cleaned_data
        # Product.objects.create(**data)
        form = ProductModelForm()
        # return HttpResponseRedirect("/success")
        # return redirect("/success")
    return render(request, "forms.html", {"form": form})

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