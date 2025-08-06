from rest_framework import generics
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer

# API View'ları
class ProductListCreateAPIView(generics.ListCreateAPIView):
    """
    Ürün listeleme ve yeni ürün oluşturma endpointi
    GET /api/products/ - Tüm ürünleri listeler
    POST /api/products/ - Yeni ürün oluşturur
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Tek bir ürün üzerinde işlem yapma endpointi
    GET /api/products/<id>/ - Tek ürün detayı
    PUT /api/products/<id>/ - Ürün güncelleme
    DELETE /api/products/<id>/ - Ürün silme
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Ana Sayfa View'ı
def home_view(request):
    """
    Ana sayfa görünümü - Projenin kök URL'si için
    """
    return HttpResponse("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Django REST API Ana Sayfa</title>
            <style>
                body { font-family: Arial, sans-serif; line-height: 1.6; margin: 40px; }
                h1 { color: #333; }
                ul { list-style-type: none; padding: 0; }
                li { margin: 10px 0; }
                a { 
                    display: inline-block;
                    padding: 10px 15px;
                    background-color: #4CAF50;
                    color: white;
                    text-decoration: none;
                    border-radius: 4px;
                }
                a:hover { background-color: #45a049; }
                .container { max-width: 800px; margin: 0 auto; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Django REST API Ana Sayfa</h1>
                <p>Mevcut API Endpointleri:</p>
                <ul>
                    <li><a href="/api/products/">/api/products/</a> - Ürün Listesi ve Ekleme</li>
                    <li><a href="/api/products/1/">/api/products/&lt;id&gt;/</a> - Tek Ürün İşlemleri</li>
                    <li><a href="/admin/">/admin/</a> - Admin Paneli</li>
                </ul>
                <p>API kullanımı için Postman veya curl gibi araçları kullanabilirsiniz:</p>
                <pre>
# Tüm ürünleri listele
curl http://127.0.0.1:8000/api/products/

# Yeni ürün ekle
curl -X POST -H "Content-Type: application/json" -d '{"name":"Örnek Ürün","price":99.99}' http://127.0.0.1:8000/api/products/
                </pre>
            </div>
        </body>
        </html>
    """)

# Template kullanımı için alternatif view (opsiyonel)
def home_template_view(request):
    """
    Template kullanarak ana sayfa oluşturma (templates/products/home.html gerektirir)
    """
    context = {
        'endpoints': [
            {'url': '/api/products/', 'description': 'Ürün Listesi ve Ekleme'},
            {'url': '/api/products/1/', 'description': 'Tek Ürün İşlemleri'},
            {'url': '/admin/', 'description': 'Admin Paneli'},
        ]
    }
    return render(request, 'products/home.html', context)