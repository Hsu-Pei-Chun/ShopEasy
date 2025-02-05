from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Product

@csrf_exempt
def product_list(request):
    if request.method == 'GET':
        products = list(Product.objects.values())  # 這樣會返回所有商品的基本信息
        # 可以將圖片URL加到每個商品中
        for product in products:
            product['image'] = product.get('image', None)  # 確保有圖片字段
        return JsonResponse({'products': products}, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        product = Product.objects.create(
            name=data['name'],
            description=data.get('description', ''),
            price=data['price'],
            stock=data.get('stock', 0)
        )
        return JsonResponse({'id': product.id, 'message': 'Product created successfully'})


@csrf_exempt
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'GET':
        return JsonResponse({
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': str(product.price),
            'stock': product.stock,
            'image': product.image.url if product.image else None,
            'created_at': product.created_at,
            'updated_at': product.updated_at,
        })

    elif request.method == 'PUT':
        data = json.loads(request.body)
        product.name = data.get('name', product.name)
        product.description = data.get('description', product.description)
        product.price = data.get('price', product.price)
        product.stock = data.get('stock', product.stock)
        product.save()
        return JsonResponse({'message': 'Product updated successfully'})

    elif request.method == 'DELETE':
        product.delete()
        return JsonResponse({'message': 'Product deleted successfully'})


# 渲染產品頁面
def product_page(request):
    return render(request, 'products/products.html')
