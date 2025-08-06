# Django REST Framework generic view'ları için gerekli modülü import ediyoruz
# generics modülü, yaygın API işlemleri için hazır view sınıfları sağlar
# Bu sınıflar, CRUD işlemlerini otomatik olarak gerçekleştirir
from rest_framework import generics

# Django HTTP response ve template rendering için gerekli modülleri import ediyoruz
# HttpResponse: Basit HTTP yanıtları oluşturmak için
# render: Template'leri render etmek için
from django.http import HttpResponse
from django.shortcuts import render

# Kendi uygulamamızdan model ve serializer'ları import ediyoruz
# Product: Veritabanı modeli
# ProductSerializer: Model verilerini JSON formatına dönüştüren serializer
from .models import Product
from .serializers import ProductSerializer

# =============================================================================
# DJANGO PRODUCTS VIEWS.PY DOSYASI
# =============================================================================
#
# Bu dosya, Django uygulamasının view'larını (görünümlerini) tanımlar.
# View'lar, HTTP isteklerini işler ve uygun yanıtları döndürür.
# Bu dosyada hem API view'ları hem de geleneksel Django view'ları bulunur.
#
# View Türleri:
# - API View'ları: REST API endpoint'leri için
# - Function View'ları: Basit HTTP yanıtları için
# - Template View'ları: HTML sayfaları için
#
# Bu dosyada tanımlanan view'lar:
# - ProductListCreateAPIView: Ürün listesi ve oluşturma API'si
# - ProductRetrieveUpdateDestroyAPIView: Ürün detay, güncelleme, silme API'si
# - home_view: Ana sayfa görünümü
# - home_template_view: Template kullanan ana sayfa (opsiyonel)
# =============================================================================

# =============================================================================
# API VIEW'LARI (Django REST Framework)
# =============================================================================

# Ürün listesi ve yeni ürün oluşturma endpoint'i
# Bu sınıf, ListCreateAPIView'dan türetilmiştir
# ListCreateAPIView, GET (liste) ve POST (oluştur) metodlarını otomatik olarak destekler
class ProductListCreateAPIView(generics.ListCreateAPIView):
    """
    Ürün listeleme ve yeni ürün oluşturma endpointi
    GET /api/products/ - Tüm ürünleri listeler
    POST /api/products/ - Yeni ürün oluşturur
    """

    # Hangi model verilerinin kullanılacağını belirtiyoruz
    # Product.objects.all() - Veritabanındaki tüm ürünleri getirir
    # Bu queryset, GET isteklerinde liste olarak döndürülür
    queryset = Product.objects.all()

    # Hangi serializer'ın kullanılacağını belirtiyoruz
    # ProductSerializer, model verilerini JSON formatına dönüştürür
    # Bu serializer, hem GET hem de POST isteklerinde kullanılır
    serializer_class = ProductSerializer

    # =============================================================================
    # OPSİYONEL ÖZELLİKLER (Şu anda kullanılmıyor)
    # =============================================================================
    #
    # Diğer yaygın ListCreateAPIView özellikleri:
    #
    # # Filtreleme ve arama
    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['name', 'price']
    # search_fields = ['name', 'description']
    # ordering_fields = ['name', 'price', 'created_at']
    # ordering = ['-created_at']  # Varsayılan sıralama
    #
    # # Sayfalama
    # pagination_class = PageNumberPagination
    #
    # # İzin kontrolü
    # permission_classes = [IsAuthenticated]
    #
    # # Özel metodlar
    # def get_queryset(self):
    #     """Özel queryset filtreleme"""
    #     return Product.objects.filter(is_active=True)
    #
    # def perform_create(self, serializer):
    #     """Ürün oluşturulurken özel işlemler"""
    #     serializer.save(created_by=self.request.user)
    # =============================================================================

# Tek bir ürün üzerinde işlem yapma endpoint'i
# Bu sınıf, RetrieveUpdateDestroyAPIView'dan türetilmiştir
# RetrieveUpdateDestroyAPIView, GET (detay), PUT/PATCH (güncelle) ve DELETE (sil) metodlarını destekler
class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Tek bir ürün üzerinde işlem yapma endpointi
    GET /api/products/<id>/ - Tek ürün detayı
    PUT /api/products/<id>/ - Ürün güncelleme
    DELETE /api/products/<id>/ - Ürün silme
    """

    # Hangi model verilerinin kullanılacağını belirtiyoruz
    # Product.objects.all() - Veritabanındaki tüm ürünleri getirir
    # URL'deki <pk> parametresi ile belirli ürün filtrelenir
    queryset = Product.objects.all()

    # Hangi serializer'ın kullanılacağını belirtiyoruz
    # ProductSerializer, model verilerini JSON formatına dönüştürür
    # Bu serializer, tüm HTTP metodlarında kullanılır
    serializer_class = ProductSerializer

    # =============================================================================
    # OPSİYONEL ÖZELLİKLER (Şu anda kullanılmıyor)
    # =============================================================================
    #
    # Diğer yaygın RetrieveUpdateDestroyAPIView özellikleri:
    #
    # # İzin kontrolü
    # permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    #
    # # Özel metodlar
    # def get_object(self):
    #     """Özel nesne alma mantığı"""
    #     pk = self.kwargs.get('pk')
    #     return get_object_or_404(Product, pk=pk, is_active=True)
    #
    # def perform_update(self, serializer):
    #     """Güncelleme sırasında özel işlemler"""
    #     serializer.save(updated_by=self.request.user)
    #
    # def perform_destroy(self, instance):
    #     """Silme sırasında özel işlemler (soft delete)"""
    #     instance.is_active = False
    #     instance.save()
    # =============================================================================

# =============================================================================
# GELENEKSEL DJANGO VIEW'LARI
# =============================================================================

# Ana sayfa görünümü - Projenin kök URL'si için
# Bu fonksiyon, kullanıcı siteye geldiğinde ilk karşılaşacağı sayfayı oluşturur
# HttpResponse ile basit HTML içeriği döndürür
def home_view(request):
    """
    Ana sayfa görünümü - Projenin kök URL'si için
    Bu view, kullanıcıya mevcut API endpoint'lerini gösterir
    ve nasıl kullanılacağı hakkında bilgi verir
    """

    # HTML içeriği ile HTTP yanıtı döndürüyoruz
    # Bu HTML, API endpoint'lerini listeleyen basit bir sayfa oluşturur
    # CSS stilleri ile görsel olarak güzel bir görünüm sağlar
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
# Bu fonksiyon, template dosyası kullanarak ana sayfa oluşturur
# render() fonksiyonu ile template'i context verisi ile render eder
def home_template_view(request):
    """
    Template kullanarak ana sayfa oluşturma (templates/products/home.html gerektirir)
    Bu view, template dosyası kullanarak daha esnek bir ana sayfa oluşturur
    Context verisi ile template'e dinamik veri gönderir
    """

    # Template'e gönderilecek context verisi
    # Bu veri, template'de kullanılabilir hale gelir
    context = {
        'endpoints': [
            {'url': '/api/products/', 'description': 'Ürün Listesi ve Ekleme'},
            {'url': '/api/products/1/', 'description': 'Tek Ürün İşlemleri'},
            {'url': '/admin/', 'description': 'Admin Paneli'},
        ]
    }

    # Template'i context verisi ile render ediyoruz
    # 'products/home.html' template dosyası gerekli
    # Bu template, context'teki endpoints verisini kullanabilir
    return render(request, 'products/home.html', context)

# =============================================================================
# OPSİYONEL VIEW TÜRLERİ (Şu anda kullanılmıyor)
# =============================================================================
#
# Diğer yaygın view türleri:
#
# # Class-based View (CBV)
# from django.views.generic import ListView, DetailView
#
# class ProductListView(ListView):
#     model = Product
#     template_name = 'products/product_list.html'
#     context_object_name = 'products'
#
# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'products/product_detail.html'
#
# # API View'ları (function-based)
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
#
# @api_view(['GET', 'POST'])
# def product_list_api(request):
#     if request.method == 'GET':
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
#
# # ViewSet (daha gelişmiş API view'ları)
# from rest_framework import viewsets
#
# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [IsAuthenticated]
# =============================================================================