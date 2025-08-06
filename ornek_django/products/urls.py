# Django URL yönlendirme için gerekli modülü import ediyoruz
# path fonksiyonu, URL desenlerini tanımlamak için kullanılır
# Bu modül, API endpoint'lerinin URL yapısını oluşturmak için gerekli
from django.urls import path

# Kendi uygulamamızdan view sınıflarını import ediyoruz
# Bu view'lar, API endpoint'lerinin işlevselliğini sağlar
# ProductListCreateAPIView: Ürün listesi ve oluşturma işlemleri
# ProductRetrieveUpdateDestroyAPIView: Ürün detay, güncelleme ve silme işlemleri
from .views import ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView

# =============================================================================
# DJANGO PRODUCTS URLS.PY API URL KONFİGÜRASYON DOSYASI
# =============================================================================
#
# Bu dosya, products uygulamasının API endpoint'lerinin URL yapısını tanımlar.
# URL patterns, gelen HTTP isteklerini hangi view'lara yönlendireceğini belirler.
# Bu dosya, ana urls.py dosyasında include() ile dahil edilir.
#
# API URL Yapısı:
# - RESTful API standartlarına uygun
# - CRUD işlemleri için ayrı endpoint'ler
# - HTTP metodları ile işlem türü belirlenir
# - URL parametreleri ile kaynak kimliği belirtilir
#
# Bu dosyada tanımlanan endpoint'ler:
# - /api/products/ (GET: Liste, POST: Oluştur)
# - /api/products/<id>/ (GET: Detay, PUT: Güncelle, DELETE: Sil)
# =============================================================================

# =============================================================================
# URL DESENLERİ TANIMLAMASI
# =============================================================================

# URL yönlendirme kuralları listesi
# Django, gelen API isteklerini bu listedeki desenlerle karşılaştırır
# İlk eşleşen desen kullanılır ve ilgili view'a yönlendirilir
urlpatterns = [
    # Ürün listesi ve oluşturma endpoint'i
    # URL: /api/products/
    # HTTP Metodları:
    #   - GET: Tüm ürünlerin listesini döndürür
    #   - POST: Yeni ürün oluşturur
    # View: ProductListCreateAPIView
    #   - ListCreateAPIView'dan türetilmiş
    #   - GET ve POST metodlarını destekler
    #   - Otomatik pagination sağlar
    #   - Serializer ile veri dönüşümü yapar
    path('products/', ProductListCreateAPIView.as_view()),

    # Ürün detay, güncelleme ve silme endpoint'i
    # URL: /api/products/<id>/
    # Örnek: /api/products/1/, /api/products/25/
    # HTTP Metodları:
    #   - GET: Belirli ürünün detaylarını döndürür
    #   - PUT/PATCH: Ürün bilgilerini günceller
    #   - DELETE: Ürünü siler
    # URL Parametresi: <int:pk>
    #   - int: Sadece integer değerler kabul eder
    #   - pk: Primary key (birincil anahtar) parametresi
    #   - View'da self.kwargs['pk'] ile erişilebilir
    # View: ProductRetrieveUpdateDestroyAPIView
    #   - RetrieveUpdateDestroyAPIView'dan türetilmiş
    #   - GET, PUT, PATCH ve DELETE metodlarını destekler
    #   - Tek bir nesne üzerinde işlem yapar
    #   - 404 hatası otomatik olarak döndürülür
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view())
]

# =============================================================================
# OPSİYONEL URL ÖZELLİKLERİ (Şu anda kullanılmıyor)
# =============================================================================
#
# Diğer yaygın URL pattern'leri:
#
# # URL isimlendirme (reverse URL lookup için)
# path('products/', ProductListCreateAPIView.as_view(), name='product-list'),
# path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
#
# # Farklı veri türleri için endpoint'ler
# path('products/categories/', CategoryListAPIView.as_view(), name='category-list'),
# path('products/search/', ProductSearchAPIView.as_view(), name='product-search'),
#
# # Nested (iç içe) URL'ler
# path('categories/<int:category_id>/products/', CategoryProductsAPIView.as_view(), name='category-products'),
#
# # Özel URL parametreleri
# path('products/<str:slug>/', ProductDetailBySlugAPIView.as_view(), name='product-detail-slug'),
# path('products/<int:pk>/reviews/', ProductReviewsAPIView.as_view(), name='product-reviews'),
#
# # Filtreleme ve sıralama parametreleri
# path('products/filter/', ProductFilterAPIView.as_view(), name='product-filter'),
# path('products/sort/', ProductSortAPIView.as_view(), name='product-sort'),
#
# # Dosya yükleme endpoint'i
# path('products/<int:pk>/image/', ProductImageUploadAPIView.as_view(), name='product-image-upload'),
# =============================================================================